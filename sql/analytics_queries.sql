-- Total predictions by damage type

SELECT
    predicted_damage,
    COUNT(*) AS total_predictions
FROM workspace.smart_claims.ai_predictions
GROUP BY predicted_damage
ORDER BY total_predictions DESC;

--------------------------------------------------

-- Total images processed

SELECT
    COUNT(*) AS total_images
FROM workspace.smart_claims.ai_predictions;

--------------------------------------------------

-- Processing volume by day

SELECT
    DATE(processed_at) AS processing_date,
    COUNT(*) AS total_processed
FROM workspace.smart_claims.ai_predictions
GROUP BY DATE(processed_at)
ORDER BY processing_date;

--------------------------------------------------

-- Data Quality Validation

SELECT
    (SELECT COUNT(*) FROM workspace.smart_claims.bronze_claim_images_stream) AS bronze_records,
    (SELECT COUNT(*) FROM workspace.smart_claims.silver_claim_images_s3) AS silver_records;
