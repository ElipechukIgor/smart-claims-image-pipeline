# Smart Claims Image Pipeline

End-to-end Lakehouse pipeline for insurance claim image processing using AWS S3, Databricks, Auto Loader, Delta Lake, MLflow and Databricks Workflows.

## Project Overview

This project simulates a real-world insurance claims processing pipeline.

Images uploaded to Amazon S3 are automatically ingested with Databricks Auto Loader, processed through a Medallion Architecture, classified using a Machine Learning model, and aggregated into analytical KPIs.

## Architecture

```text
AWS S3
  ↓
Databricks Auto Loader
  ↓
Bronze Layer
  ↓
Silver Layer
  ↓
AI Inference
  ↓
Gold KPIs
  ↓
Dashboard
  ↓
Databricks Workflow
```

## Technologies

* AWS S3
* Databricks
* PySpark
* Structured Streaming
* Auto Loader
* Delta Lake
* MLflow
* Scikit-learn
* Databricks Workflows
* Data Quality Checks

## Pipeline Layers

### Bronze Layer

Raw image ingestion from Amazon S3 using Auto Loader.

### Silver Layer

Metadata extraction from image paths, including:

* file name
* damage type
* file size
* ingestion timestamp

### AI Inference Layer

Machine Learning model used to classify claim images by damage type.

Example output:

| file_name      | predicted_damage |
| -------------- | ---------------- |
| claim_1004.jpg | colisao          |
| claim_2003.jpg | enchente         |
| claim_3002.jpg | incendio         |

### Gold Layer

Business KPIs generated from predictions.

| predicted_damage | total_predictions |
| ---------------- | ----------------: |
| colisao          |                 4 |
| enchente         |                 2 |
| incendio         |                 1 |

## Workflow

The pipeline is orchestrated using Databricks Workflows:

```text
bronze_ingestion
  ↓
silver_metadata
  ↓
ai_inference
  ↓
gold_ai_prediction_kpis
  ↓
data_quality_checks
```

## Data Quality

The project includes validation checks to compare records between Bronze and Silver layers and ensure pipeline consistency.

## Results

The final pipeline includes:

* Incremental image ingestion
* Checkpoint-based processing
* Bronze/Silver/Gold architecture
* AI-based image classification
* Gold analytical KPIs
* Databricks Workflow orchestration

## Author

Igor Elipechuk
Data Engineering | Databricks | AWS | PySpark | MLflow

