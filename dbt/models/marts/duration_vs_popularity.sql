SELECT DISTINCT 
    track_name, 
    artist_name, 
    duration, 
    SUM(listeners) total_listeners
FROM {{ref('stg_top_tracks')}}
WHERE duration > 0
GROUP BY track_name, artist_name, duration
ORDER BY total_listeners DESC