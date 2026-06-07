# Databricks notebook source
silver_df = spark.table(
    "workspace.smart_claims.silver_claim_images_s3"
)

silver_df.display()

# COMMAND ----------

from pyspark.sql.functions import count

gold_df = (
    silver_df
    .groupBy("damage_type")
    .agg(
        count("*").alias("total_images")
    )
)

# COMMAND ----------

gold_df.display()

# COMMAND ----------

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "workspace.smart_claims.gold_claim_images_s3"
    )

# COMMAND ----------

spark.sql("""
SELECT *
FROM workspace.smart_claims.gold_claim_images_s3
""").display()