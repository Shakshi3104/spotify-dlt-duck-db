with final as (
    select
        id as track_id,
        name as track_title

    from {{ source('bronze', 'tracks') }}
)

select * from final