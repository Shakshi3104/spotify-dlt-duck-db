with final as (
    select
        id as track_id,
        album__id as album_id,
        duration_ms,
        external_ids__isrc as isrc,
        external_urls__spotify as spotify_url,
        popularity

    from {{ source('bronze', 'track_details') }}
)

select * from final