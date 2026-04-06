WITH 
stg as 
(SELECT DISTINCT
        artist_name, 
        country
        FROM {{ ref('stg_top_tracks') }})

SELECT 
    artist_name, 
    count(country) country_count
FROM stg
GROUP BY artist_name  
ORDER BY count(country) DESC

