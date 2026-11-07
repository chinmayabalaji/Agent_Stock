create schema if not exists bronze;

create schema if not exists silver;

create schema if not exists gold;

create table if not exists bronze.stocks_raw (
    source_filename varchar(100) not null,
    row_number int not null,
    json_data super not null,
    ingested_at timestamp default GETDATE()
);

create table if not exists silver.stocks_hist (
    symbol varchar(10) not null,
    series varchar(50) not null,
    isin varchar(100) not null,
    open double,
    high double,
    low double,
    close double,
    last double,
    prev_close double,
    volume double,
    turnover double,
    trades double,
    row_effective_start_date timestamp not null,
    row_effective_end_date timestamp not null,
    active_flag varchar(1) not null
)

create table if not exists gold.stocks_snap (
    symbol varchar(10) not null,
    series varchar(50) not null,
    isin varchar(100) not null,
    open double,
    high double,
    low double,
    close double,
    last double,
    prev_close double,
    volume double,
    turnover double,
    trades double
)