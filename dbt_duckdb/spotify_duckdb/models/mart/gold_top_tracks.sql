with final as (
    select
        top_tracks.id,
        top_tracks.name as song_title,
        top_tracks.album__name as album_title,
        artists.name as artist_name,
        top_tracks.external_urls__spotify as spotify_url,
        top_tracks.popularity
    from {{ source('bronze', 'top_tracks') }} as top_tracks

    left join {{ source('bronze', 'top_tracks__album__artists') }} as artists
    using (_dlt_id)
)

select * from final