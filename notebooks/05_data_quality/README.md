# Data Quality Layer

## Purpose

This layer validates data consistency across Bronze, Silver and Gold layers.

The goal is to ensure pipeline reliability and trustworthy analytics.

---

## Validation Checks

- Bronze record count validation
- Silver record count validation
- Missing metadata detection
- Null value checks
- Pipeline consistency verification

---

## Example Validation

| Layer | Records |
|---------|---------:|
| Bronze | 7 |
| Silver | 7 |

---

## Expected Result

```text
PASS
```

when record counts match.

---

## Business Value

Ensures data integrity and prevents analytical discrepancies across the Lakehouse pipeline.
