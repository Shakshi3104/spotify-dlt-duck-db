import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_spotify_access_token(is_dict=False) -> str | dict:
    # Load env variables
    load_dotenv()

    # Get Spotify Web API access token
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    credentials = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    access_token = credentials.get_access_token()

    if is_dict:
        return access_token
    else:
        return access_token["access_token"]