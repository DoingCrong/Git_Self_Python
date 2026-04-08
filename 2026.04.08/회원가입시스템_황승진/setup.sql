create database if not exists memberdb;
use memberdb;

create table if not exists members (
    id       varchar(50)  primary key,
    password varchar(100) not null,
    phone    varchar(20),
    birth    date,
    address  varchar(200),
    hobby    varchar(100),
    gender   varchar(5),
    note     text
);
