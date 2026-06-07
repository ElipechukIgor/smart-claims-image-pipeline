# Gold Layer

## Purpose

The Gold layer generates business KPIs and analytical datasets from Machine Learning predictions.

This layer provides aggregated information ready for dashboards and decision-making.

---

## Input Tables

```text
workspace.smart_claims.ai_predictions
```

---

## Output Tables

```text
workspace.smart_claims.gold_claim_images_s3

workspace.smart_claims.gold_ai_prediction_kpis
```

---

## Generated KPIs

- Total predictions by damage type
- Processing volume
- Operational metrics
- AI prediction distribution

---

## Example

| predicted_damage | total_predictions |
|------------------|------------------:|
| colisao | 4 |
| enchente | 2 |
| incendio | 1 |

---

## Business Value

Provides real-time visibility into insurance claim volumes and damage trends.
