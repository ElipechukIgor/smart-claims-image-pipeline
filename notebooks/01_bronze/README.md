# Bronze Layer

## Purpose

The Bronze layer is responsible for ingesting raw insurance claim images from AWS S3 using Databricks Auto Loader.

This layer serves as the landing zone of the Lakehouse architecture and stores data exactly as received from the source system.

---

## Main Features

- AWS S3 integration
- Databricks Auto Loader
- Structured Streaming
- Incremental ingestion
- Checkpoint management
- Delta Lake storage

---

## Input

```text
s3://smart-claims-lakehouse-igor-2026/raw/images/
```

---

## Output Table

```text
workspace.smart_claims.bronze_claim_images_stream
```

---

## Stored Metadata

- path
- modificationTime
- length
- content

---

## Business Value

Provides scalable and fault-tolerant ingestion of incoming claim images for downstream processing.
