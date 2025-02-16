import dlt
from dlt.sources.rest_api import (
    RESTAPIConfig,
    check_connection,
    rest_api_resources,
    rest_api_source,
)
from dlt.sources.helpers import requests


def top_tracks(artist_id: str, access_token: str) -> dlt.sources.DltSource:
    """
    dlt source of top tracks from artist_id

    Parameters
    ----------
    artist_id: str
        Spotify ID of the artist
    access_token: str
        Spotify access token

    Returns
    -------
    source: DltSource
    """
    # Base URL
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

    # REST API source
    source = rest_api_source(config)

    return source


def tracks(artist_id: str, access_token: str) -> dlt.sources.DltSource:
    """
    dlt source of tracks from artist_id

    Parameters
    ----------
    artist_id: str
        Spotify ID of the artist
    access_token: str
        Spotify access token

    Returns
    -------
    source: DltSource
    """
    # Base URL
    base_url = f"https://api.spotify.com/v1/"

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
            # https://api.spotify.com/v1/artists/{artist_id}/albums
            {
                "name": "albums",
                "endpoint": {
                    "path": f"artists/{artist_id}/albums",
                    "params": {
                        "market": "JP"
                    }
                }
            },
            # https://api.spotify.com/v1/albums/{album_id}/tracks
            {
                "name": "tracks",
                "endpoint": {
                    "path": "albums/{album_id}/tracks",
                    "params": {
                        "market": "JP",
                        "album_id": {
                            "type": "resolve",
                            "resource": "albums",
                            "field": "id"
                        }
                    }
                }
            },
            # https://api.spotify.com/v1/tracks/{track_id}
            {
                "name": "track_details",
                "endpoint": {
                    "path": "tracks/{track_id}",
                    "params": {
                        "market": "JP",
                        "track_id": {
                            "type": "resolve",
                            "resource": "tracks",
                            "field": "id"
                        }
                    }
                }
            }
        ],
    }

    # REST API source
    source = rest_api_source(config)

    return source


if __name__ == "__main__":
    from spotify_credentials import get_spotify_access_token

    access_token = get_spotify_access_token()

    url = "https://api.spotify.com/v1/audio-features/4mpxYAluelzjpNwBJUJx32?market=JP"
    response = requests.get(
        url,
        headers={
            'Authorization': f"Bearer {access_token}"
        }
    )
    data = response.json()
