# Databricks notebook source
bronze_count = spark.sql("""
SELECT COUNT(*) total
FROM workspace.smart_claims.bronze_claim_images_stream
""").collect()[0]["total"]

silver_count = spark.sql("""
SELECT COUNT(*) total
FROM workspace.smart_claims.silver_ai_claim_predictions
""").collect()[0]["total"]

assert bronze_count == silver_count, \
    f"Inconsistência: Bronze={bronze_count}, Silver={silver_count}"

print("Data Quality Check OK")