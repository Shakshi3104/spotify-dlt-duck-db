with all_track_details as (
    select
        track_details.track_id,
        tracks.track_title,
        track_details.album_id,
        track_details.popularity,
        track_details.spotify_url

    from {{ ref('sliver_track_details') }} as track_details
    left join {{ ref('sliver_tracks') }} as tracks
    using (track_id)
),
-- Remove duplicates by track_title
-- Keep the one with the largest popularity
final as (
    select * exclude (row_num)
    from (
        select
            row_number() over (
                partition by track_title
                order by popularity desc
            ) as row_num,
            *
        from all_track_details
    )
    where row_num = 1
)

select * from final