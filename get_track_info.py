from dotenv import load_dotenv
import os as os
import requests
import json
import time 

load_dotenv()

last_fm_key = os.getenv("LASTFM_API_KEY")

api_root_url = 'http://ws.audioscrobbler.com/2.0'



file_path = "deduped_artists.json"

with open(file_path, "r", encoding="utf-8") as file:
    artists = json.load(file)  
    
all_artist_tag = []

for artist_ in artists:
    artist = artist_["artist_name"]
    
    try:
        response = requests.get(f"{api_root_url}/?method=artist.getTopTags&api_key={last_fm_key}&artist={artist}&format=json")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
        continue 
    time.sleep(0.2)
    data = response.json()
    if "error" in data.keys():
        print(f"Errored out due to error code {data["error"]}: {data["message"]}")
        continue
    
    tags = data["toptags"]["tag"]
    artist_tag = []
    for tag in tags:
        artist_tag.append(tag["name"])
    all_artist_tag.append({"artist":artist,
                           "tags":artist_tag})

with open("artist_tags.json", "w") as f:
    json.dump(all_artist_tag, f)