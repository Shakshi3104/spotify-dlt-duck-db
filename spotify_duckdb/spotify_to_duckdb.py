import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import dlt
from dlt.sources.rest_api import (
    RESTAPIConfig,
    check_connection,
    rest_api_resources,
    rest_api_source,
)
from dlt.sources.helpers import requests

from spotify_credentials import get_spotify_access_token
from spotify_api_sources import tracks


if __name__ == "__main__":
    load_dotenv()

    # Get Spotify access token
    access_token: str = get_spotify_access_token()

    # Extract data from REST API
    # Get data of Naniwa Danshi
    artist_id = "5V0oa9WaeYkBszHV6ItVD6"
    # Get all tracks
    source = tracks(artist_id, access_token)

    # Pipeline configuration
    pipeline = dlt.pipeline(
        pipeline_name="spotify_api_example",
        destination="duckdb",
        dataset_name="naniwa_danshi",
        # refresh dataset
        refresh="drop_sources"
    )

    # Run the pipeline
    load_info = pipeline.run(source)
