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

if __name__ == "__main__":
    load_dotenv()

    # Get Spotify Web API access token
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    credentials = SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )

    access_token = credentials.get_access_token()

    # Extract data from REST API
    # Get data of Naniwa Danshi
    artist_id = "5V0oa9WaeYkBszHV6ItVD6"
    base_url = f"https://api.spotify.com/v1/artists/{artist_id}/"

    # REST API configuration
    config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": (
                {
                    "type": "bearer",
                    "token": access_token["access_token"],
                }
                if access_token
                else None
            )
        },
        "resources": [
            {
                "name": "top-tracks",
                "endpoint": {
                    "path": "top-tracks"
                }
            },
            {
                "name": "albums",
                "endpoint": {
                    "path": "top-tracks",
                    "data_selector": "tracks.album"
                }
            }
        ],
    }

    # Pipeline configuration
    source = rest_api_source(config)

    pipeline = dlt.pipeline(
        pipeline_name="spotify_api_example",
        destination="duckdb",
        dataset_name="naniwa_top_tracks"
    )

    # Run the pipeline
    load_info = pipeline.run(source)
