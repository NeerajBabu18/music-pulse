from prefect import task, flow
from get_top_tracks import get_top_tracks
from get_track_info import get_track_info
from load_to_bigquery import load_to_bigquery

import subprocess

@task
def run_dbt():
    subprocess.run(["dbt", "run"], cwd="dbt/", check=True)

@task
def test_dbt():
    subprocess.run(["dbt", "test"], cwd="dbt/", check=True)
    
@flow
def music_pulse_pipeline():
    tracks_result = get_top_tracks()
    info_result = get_track_info(wait_for=[tracks_result])
    load_result = load_to_bigquery(wait_for=[info_result])
    dbt_run_result = run_dbt(wait_for=[load_result])
    test_dbt(wait_for=[dbt_run_result])
    
    
if __name__ == "__main__":
    music_pulse_pipeline()