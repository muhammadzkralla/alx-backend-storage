-- Get all the bands with glam style ranked by lifespan

SELECT band_name, COALESCE(split, 2022) - formed as lifespan
FROM metal_bands
WHERE style like '%Glam rock%';