# AI Inference Layer

## Purpose

This layer performs Machine Learning inference on claim image metadata.

The objective is to automatically classify insurance claim images according to the type of damage.

---

## Technologies

- Python
- PySpark
- Scikit-learn
- MLflow
- Databricks

---

## Input Table

```text
workspace.smart_claims.silver_claim_images_s3
```

---

## Output Table

```text
workspace.smart_claims.ai_predictions
```

---

## Example Predictions

| file_name | predicted_damage |
|------------|------------------|
| claim_1004.jpg | colisao |
| claim_2003.jpg | enchente |
| claim_3002.jpg | incendio |

---

## Business Value

Reduces manual effort in claim classification and accelerates insurance processing workflows.
