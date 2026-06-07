# Databricks notebook source
bronze_stream = (
    spark.readStream
         .format("cloudFiles")
         .option("cloudFiles.format", "binaryFile")
         .load(
             "s3://smart-claims-lakehouse-igor-2026/raw/images/*"
         )
)

# COMMAND ----------

bronze_stream.printSchema()

# COMMAND ----------

(
    bronze_stream.writeStream
    .format("delta")
    .outputMode("append")
    .option(
        "checkpointLocation",
        "s3://smart-claims-lakehouse-igor-2026/checkpoints/bronze_images"
    )
    .trigger(availableNow=True)
    .toTable(
        "workspace.smart_claims.bronze_claim_images_stream"
    )
)

# COMMAND ----------

spark.sql("""
SELECT *
FROM workspace.smart_claims.bronze_claim_images_stream
""").display()