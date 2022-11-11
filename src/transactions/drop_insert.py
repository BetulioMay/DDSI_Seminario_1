
def drop_tables(cursor) :
    drop_stock = "drop table stock"
    drop_order = "drop table pedido"
    drop_details = "drop table detalle_pedido"
    try:
        cursor.execute(drop_details)
        cursor.execute(drop_stock)
        cursor.execute(drop_order)
    except Exception as e: 
        print(e)
        return False
    return True

def insert_tables(cursor) :
    insert_stock = "create table stock (Cproducto int not null primary key,cantidad int default 0)"
    insert_order = "create table pedido (Cpedido int not null primary key,Ccliente int not null,fecha_pedido date)"
    insert_details = "create table detalle_pedido (Cproducto references stock(Cproducto),Cpedido references pedido(Cpedido),cantidad int default 1,primary key (Cproducto, Cpedido))"
    try:
        cursor.execute(insert_stock)
        cursor.execute(insert_order)
        cursor.execute(insert_details)
    except Exception as e: 
        print(e)
        return False
    return True

