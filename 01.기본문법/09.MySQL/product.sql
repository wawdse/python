create database shop;
use shop;

create table product(
	code char(3) primary key,
    name varchar(300) not null,
    price int default 0
);

desc product;

insert into product(code, name, price)
values('101', '냉장고', 3500000);
insert into product(code, name, price)
values('102', '세탁기', 2300000);
insert into product(code, name, price)
values('103', '스타일러', 1700000);
select * from product;

create table sale(
	seq int primary key auto_increment,
    code char(3) not null,
    date datetime not null,
    qnt int default 0,
    price int default 0,
    foreign key(code) references product(code)
);
drop table sale;
desc sale;

insert into sale(code, date, qnt, price)
values('101', now(), 12, 3250000);
insert into sale(code, date, qnt, price)
values('102', now(), 5, 2100000);
insert into sale(code, date, qnt, price)
values('103', now(), 6, 1500000);
insert into sale(code, date, qnt, price)
values('103', now(), 15, 1700000);

select * from sale;

commit;