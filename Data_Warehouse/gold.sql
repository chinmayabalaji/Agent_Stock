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
);