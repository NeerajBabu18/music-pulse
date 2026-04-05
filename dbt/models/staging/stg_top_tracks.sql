SELECT track_name,
        duration,
        artist_name,
        listeners,
        position,
        country,
        CASE 
        WHEN LOWER(REPLACE(tags, '-', ' ')) IN ('kpop', 'k pop') THEN 'k-pop'
        ELSE LOWER(REPLACE(tags, '-', ' '))
        END AS tags
FROM `music-pulse-492116.raw.top_tracks_by_nation` WHERE tags IS NOT NULL