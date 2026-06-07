# Databricks notebook source
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np

from PIL import Image
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

model_info = spark.sql("""
SELECT *
FROM workspace.smart_claims.ml_model_registry
LIMIT 1
""").toPandas()

run_id = model_info.iloc[0]["run_id"]

model_uri = f"runs:/{run_id}/model"

model = mlflow.sklearn.load_model(model_uri)

print("Modelo carregado:", model_uri)

# COMMAND ----------

bronze_df = spark.table(
    "workspace.smart_claims.bronze_claim_images_stream"
)

images_pd = bronze_df.select(
    "path",
    "length",
    "modificationTime"
).toPandas()

display(images_pd)

# COMMAND ----------

def extract_image_features(image_path):
    local_path = image_path.replace("s3://", "/dbfs/mnt/")

    try:
        img = Image.open(image_path).convert("RGB")
    except:
        binary_df = spark.read.format("binaryFile").load(image_path)
        content = binary_df.select("content").collect()[0]["content"]

        from io import BytesIO
        img = Image.open(BytesIO(content)).convert("RGB")

    img = img.resize((128, 128))

    arr = np.array(img)

    width, height = img.size

    return {
        "width": width,
        "height": height,
        "aspect_ratio": width / height,
        "mean_r": arr[:, :, 0].mean(),
        "mean_g": arr[:, :, 1].mean(),
        "mean_b": arr[:, :, 2].mean(),
        "std_r": arr[:, :, 0].std(),
        "std_g": arr[:, :, 1].std(),
        "std_b": arr[:, :, 2].std()
    }

# COMMAND ----------

feature_rows = []

for _, row in images_pd.iterrows():
    try:
        features = extract_image_features(row["path"])

        file_name = row["path"].split("/")[-1]

        features["file_name"] = file_name
        features["path"] = row["path"]
        features["length"] = row["length"]
        features["modificationTime"] = row["modificationTime"]

        feature_rows.append(features)

    except Exception as e:
        print("Erro ao processar:", row["path"], e)

features_pd = pd.DataFrame(feature_rows)

display(features_pd)

# COMMAND ----------

feature_cols = [
    "width",
    "height",
    "aspect_ratio",
    "mean_r",
    "mean_g",
    "mean_b",
    "std_r",
    "std_g",
    "std_b",
    "length"
]

features_pd["predicted_damage"] = model.predict(
    features_pd[feature_cols]
)

# COMMAND ----------

features_pd["claim_id"] = (
    features_pd["file_name"]
    .str.extract(r"claim_(\d+)")
    .astype(int)
)

# COMMAND ----------

predictions_pd = features_pd[
    [
        "claim_id",
        "file_name",
        "path",
        "predicted_damage",
        "length",
        "modificationTime"
    ]
]

display(predictions_pd)

# COMMAND ----------

predictions_df = spark.createDataFrame(predictions_pd)

predictions_df = predictions_df.withColumn(
    "prediction_timestamp",
    current_timestamp()
)

predictions_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "workspace.smart_claims.silver_ai_claim_predictions"
    )

# COMMAND ----------

spark.sql("""
SELECT
    claim_id,
    file_name,
    predicted_damage,
    prediction_timestamp
FROM workspace.smart_claims.silver_ai_claim_predictions
ORDER BY claim_id
""").display()