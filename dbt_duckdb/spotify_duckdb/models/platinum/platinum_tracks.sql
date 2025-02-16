with final as (
    select
        tracks.track_title,
        albums.album_title,
        tracks.popularity,
        tracks.spotify_url,
        albums.release_date

    from {{ ref('gold_tracks') }} as tracks
    left join {{ ref('gold_albums') }} as albums
    using (album_id)
)

select * from final