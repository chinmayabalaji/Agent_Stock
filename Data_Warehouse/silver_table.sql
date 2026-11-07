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
);