WITH track_rank as (SELECT DISTINCT country,
        tags,
        RANK() OVER (PARTITION BY country ORDER BY COUNT(track_name) DESC) AS tag_rank,
        COUNT(track_name) AS track_count
FROM {{ ref('stg_top_tracks') }} 
GROUP BY country, tags)
SELECT * from track_rank WHERE tag_rank <= 5