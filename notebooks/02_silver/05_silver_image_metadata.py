# Databricks notebook source
from pyspark.sql.functions import regexp_extract
from pyspark.sql.functions import split
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

bronze_df = spark.table(
    "workspace.smart_claims.bronze_claim_images_s3"
)

# COMMAND ----------

silver_df = bronze_df.withColumn(
    "damage_type",
    regexp_extract(
        "path",
        r"images/([^/]+)/",
        1
    )
)

# COMMAND ----------

from pyspark.sql.functions import element_at

silver_df = silver_df.withColumn(
    "file_name",
    element_at(split("path","/"), -1)
)

# COMMAND ----------

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(
        "workspace.smart_claims.silver_claim_images_s3"
    )

# COMMAND ----------

spark.sql("""
SELECT
    file_name,
    damage_type,
    length,
    ingestion_timestamp
FROM workspace.smart_claims.silver_claim_images_s3
""").display()