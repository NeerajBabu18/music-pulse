from dotenv import load_dotenv
import os as os
import requests
import json

load_dotenv()

last_fm_key = os.getenv("LASTFM_API_KEY")

api_root_url = 'http://ws.audioscrobbler.com/2.0'

country = 'India'

response = requests.get(f"{api_root_url}/?method=geo.gettoptracks&country={country}&api_key={last_fm_key}&format=json&limit=5&page=1")

tracks_dict = response.json()

tracks = tracks_dict["tracks"]["track"]

cleaned_tracks = []

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

print(cleaned_tracks)