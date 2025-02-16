with final as (
    select
        id as album_id,
        name as album_title,
        cast(release_date as date) as release_date,
        album_type,
        total_tracks,
        external_urls__spotify as spotify_url
    from {{ source('bronze', 'albums') }}
)

select * from final