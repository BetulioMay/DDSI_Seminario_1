
def drop_tables(cursor) :
  drop_details = "drop table detalle_pedido"
  drop_order = "drop table pedido"
  drop_stock = "drop table stock"
  try:
      cursor.execute(drop_details)
      cursor.execute(drop_order)
      cursor.execute(drop_stock)
  except Exception as e: 
      print(e)
      return False
  return True

def insert_tables(cursor) :
    insert_stock = "create table stock (Cproducto int not null primary key,cantidad int default 0)"
    insert_stock_tuplas1 = "insert into stock values(134521,20)"
    insert_stock_tuplas2 = "insert into stock values(224421,10)"
    insert_stock_tuplas3 = "insert into stock values(352343,5)"
    insert_stock_tuplas4 = "insert into stock values(242421,30)"
    insert_stock_tuplas5 = "insert into stock values(678991,20)"
    insert_stock_tuplas6 = "insert into stock values(546738,15)"
    insert_stock_tuplas7 = "insert into stock values(298732,40)"
    insert_stock_tuplas8 = "insert into stock values(846538,70)"
    insert_stock_tuplas9 = "insert into stock values(982574,8)"
    insert_stock_tuplas10 = "insert into stock values(172764,90)"
    insert_order = "create table pedido (Cpedido int not null primary key,Ccliente int not null,fecha_pedido date)"
    insert_details = "create table detalle_pedido (Cproducto references stock(Cproducto),Cpedido references pedido(Cpedido),cantidad int default 1,primary key (Cproducto, Cpedido))"
    try:
        cursor.execute(insert_stock)
        cursor.execute(insert_stock_tuplas1)
        cursor.execute(insert_stock_tuplas2)
        cursor.execute(insert_stock_tuplas3)
        cursor.execute(insert_stock_tuplas4)
        cursor.execute(insert_stock_tuplas5)
        cursor.execute(insert_stock_tuplas6)
        cursor.execute(insert_stock_tuplas7)
        cursor.execute(insert_stock_tuplas8)
        cursor.execute(insert_stock_tuplas9)
        cursor.execute(insert_stock_tuplas10)
        cursor.execute(insert_order)
        cursor.execute(insert_details)
    except Exception as e: 
        print(e)
        return False
    return True

def create_tables(cursor) :
	insert_stock = "create table stock (Cproducto int not null primary key,cantidad int default 0)"
	insert_order = "create table pedido (Cpedido int not null primary key,Ccliente int not null,fecha_pedido date)"
	insert_details = "create table detalle_pedido (Cpedido references pedido(Cpedido),Cproducto references stock(Cproducto),cantidad int default 1,primary key (Cpedido, Cproducto))"
	try:
		cursor.execute(insert_stock)
		cursor.execute(insert_order)
		cursor.execute(insert_details)
	except Exception as e: 
		print(e)
		return False
	return True
