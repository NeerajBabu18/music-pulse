# music-pulse

Music Pulse is an end to end data engineering project that analyses global music trends using Last.fm data, built with Python, BigQuery, dbt, Prefect, and Looker Studio.

# Problem Statement

What makes a song trend globally on Last.fm, and does it differ by region or genre?

# Architecture

Last.fm API → Python ingestion (get_top_tracks.py, get_track_info.py) → BigQuery raw dataset → dbt transformations → BigQuery transformed dataset → Looker Studio dashboard. The pipeline is orchestrated end-to-end using Prefect.

 # Tech Stack

 1. Big Query
 2. dbt
 3. prefect
 4. looker studio
 5. Python

 # How to run

1. Clone the repository
2. Create a virtual environment: python3 -m venv venv && source venv/bin/activate
3. Install dependencies: pip install -r requirements.txt
4. Create a .env file with the following variables:
   LASTFM_API_KEY=your_last_fm_api_key
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/gcp/keyfile.json
5. Set up a BigQuery project and create datasets: raw and transformed
6. Run the pipeline: python pipeline.py

 # Dashboard link

 https://lookerstudio.google.com/reporting/42a1d598-0681-46bf-a144-079975864853

 # Key Insights

 K-pop dominates trending charts across Asian markets, with BTS appearing in 9 out of 10 countries, the broadest global reach of any artist in the dataset. While hip hop and pop are the most common genres globally, the US notably skews toward hip hop over K-pop, suggesting regional taste differences. However, Last.fm's user base is smaller in the US relative to other markets, which may affect the representativeness of these findings.

