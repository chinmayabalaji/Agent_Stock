create table if not exists bronze.stocks_raw (
    source_filename varchar(100) not null,
    row_number int not null,
    json_data super not null,
    ingested_at timestamp default GETDATE()
);