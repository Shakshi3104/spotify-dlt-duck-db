import duckdb


if __name__ == "__main__":
    duckdb_connection = 'spotify_api_example.duckdb'

    spotify_data = duckdb.connect(duckdb_connection)
    rel = spotify_data.sql(
        """
        select name, popularity, album__name, external_urls__spotify
        from naniwa_danshi.track_details
        """
    )
    rel.show()

