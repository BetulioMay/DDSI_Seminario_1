import cx_Oracle

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

