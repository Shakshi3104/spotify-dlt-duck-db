import duckdb


if __name__ == "__main__":
    duckdb_connection = 'spotify_api_example.duckdb'

    spotify_data = duckdb.connect(duckdb_connection)
    rel = spotify_data.sql(
        """
        select
            song_title, album_title, popularity
        from gold_top_tracks
        """
    )
    rel.show()
