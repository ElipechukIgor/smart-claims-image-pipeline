# Silver Layer

## Purpose

The Silver layer transforms raw image data into structured metadata.

This layer extracts relevant information from image paths and prepares data for Machine Learning inference.

---

## Transformations

- File name extraction
- Damage type extraction
- File size extraction
- Ingestion timestamp generation

---

## Input Table

```text
workspace.smart_claims.bronze_claim_images_stream
```

---

## Output Table

```text
workspace.smart_claims.silver_claim_images_s3
```

---

## Generated Columns

| Column |
|----------|
| file_name |
| damage_type |
| length |
| ingestion_timestamp |

---

## Example

| file_name | damage_type |
|------------|------------|
| claim_1004.jpg | colisao |
| claim_2003.jpg | enchente |
| claim_3002.jpg | incendio |

---

## Business Value

Creates a clean and analytics-ready dataset for Machine Learning and reporting.
