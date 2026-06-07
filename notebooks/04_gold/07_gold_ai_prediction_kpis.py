# Databricks notebook source
from pyspark.sql.functions import count, current_timestamp

predictions_df = spark.table(
    "workspace.smart_claims.silver_ai_claim_predictions"
)

gold_ai_df = (
    predictions_df
    .groupBy("predicted_damage")
    .agg(
        count("*").alias("total_predictions")
    )
    .withColumn(
        "processed_at",
        current_timestamp()
    )
)

gold_ai_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "workspace.smart_claims.gold_ai_prediction_kpis"
    )

# COMMAND ----------

spark.sql("""
SELECT *
FROM workspace.smart_claims.gold_ai_prediction_kpis
ORDER BY total_predictions DESC
""").display()