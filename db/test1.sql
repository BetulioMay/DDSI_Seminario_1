
create table stock (
    Cproducto int not null primary key,
    cantidad int default 0
);


create table pedido (
    Cpedido int not null primary key,
    Ccliente int not null,
    fecha_pedido date
);

create table detalle_pedido (
    Cproducto references stock(Cproducto),
    Cpedido references pedido(Cpedido),
    cantidad int default 1,
    primary key (Cproducto, Cpedido)
);

select * from stock;
insert into stock values (1, 10);
insert into stock values (2, 23);
insert into stock values (3, 15);
insert into stock values (4, 4);

select * from pedido;
insert into pedido values (1, 1, sysdate);
insert into pedido values (2, 2, sysdate);
insert into pedido values (3, 3, sysdate);
insert into pedido values (4, 4, sysdate);

select * from detalle_pedido;

select cantidad from stock where cproducto=1;
/* Drop tables */
drop table detalle_pedido;
drop table pedido;
drop table stock;