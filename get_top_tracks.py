from dotenv import load_dotenv
import os as os
import requests
import json
from prefect import task




@task
def get_top_tracks():
    
    load_dotenv()

    last_fm_key = os.getenv("LASTFM_API_KEY")
    
    api_root_url = 'http://ws.audioscrobbler.com/2.0'
    countries = [
        "India",
        "China",
        "United States",
        "Indonesia",
        "Pakistan",
        "Nigeria",
        "Brazil",
        "Bangladesh",
        "Russian Federation",
        "Mexico"
    ]

    cleaned_tracks = []
    deduped_artists_ = []

    for country in countries:
        print(country)
        try:
            response = requests.get(f"{api_root_url}/?method=geo.gettoptracks&country={country}&api_key={last_fm_key}&format=json&limit=50&page=1")
        except requests.exceptions.RequestException as err:
            print(f"An unexpected error occurred: {err}")
            continue
        tracks_dict = response.json()
        
        if "error" in tracks_dict.keys():
            print(f"Errored out due to error code {tracks_dict["error"]}: {tracks_dict["message"]}")
            continue
    
        tracks = tracks_dict["tracks"]["track"]
        
        for track in tracks:
            track_name = track["name"]
            duration = track["duration"]
            listeners = track["listeners"]
            position = track["@attr"]["rank"]
            artist_name = track["artist"]["name"]
            cleaned_tracks.append({"track_name":track_name,
                                "duration": duration,
                                "artist_name":artist_name,
                                "listeners":listeners,
                                "position":position,
                                "country":country
                                })
            deduped_artists_.append({"artist_name":artist_name})
        
        print("Finished",country)
        
    deduped_artists = [dict(t) for t in {tuple(d.items()) for d in deduped_artists_}]


    with open("deduped_artists.json", "w") as f:
        json.dump(deduped_artists, f)
        

    with open("all_tracks.json", "w") as f:
        json.dump(cleaned_tracks, f)