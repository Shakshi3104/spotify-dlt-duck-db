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


if __name__ == "__main__":
    load_dotenv()

    # Get Spotify access token
    access_token: str = get_spotify_access_token()

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
                    "token": access_token,
                }
                if access_token
                else None
            )
        },
        "resources": [
            {
                "name": "top-tracks",
                "endpoint": {
                    "path": "top-tracks",
                    "params": {
                        "market": "JP"
                    }
                }
            }
        ],
    }

    # Pipeline configuration
    source = rest_api_source(config)

    pipeline = dlt.pipeline(
        pipeline_name="spotify_api_example",
        destination="duckdb",
        dataset_name="naniwa_top_tracks",
        # refresh dataset
        refresh="drop_sources"
    )

    # Run the pipeline
    load_info = pipeline.run(source)
