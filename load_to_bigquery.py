import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv
import os
from prefect import task


@task
def load_to_bigquery():
    load_dotenv()


    client = bigquery.Client()

    tracks = pd.read_json("all_tracks.json")
    tags = pd.read_json("artist_tags.json")

    tags_explode = tags.explode('tags')

    print(tags_explode.head())

    tracks_with_tags = pd.merge(tracks, tags_explode, how="left", left_on="artist_name", right_on="artist").drop_duplicates()

    tracks_with_tags.drop(columns="artist",inplace=True)

    project_id = "music-pulse-492116"
    dataset_id = "raw"
    table_id = "top_tracks_by_nation"

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    dataset_ref = f"{project_id}.{dataset_id}"
    client.create_dataset(dataset_ref, exists_ok=True)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"  # overwrite table each run
    )

    job = client.load_table_from_dataframe(tracks_with_tags, table_ref, job_config=job_config)

    job.result()

    print(f"Loaded {len(tracks_with_tags)} rows into {table_ref}")
