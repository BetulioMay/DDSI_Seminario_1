
import interfaces.order as order
import interfaces.detail_order as detail
from constants import ORDER_OPTION
import helpers as h

import sys

# Inserta un nuevo pedido a la tabla Pedido
def insert_basic_data(cursor):
	order_id, client_id, order_date = order.get_order_data()

	sql = '''
		INSERT INTO pedido VALUES (:ordid, :clid, :orddt)
	'''
	cursor.execute(sql, ordid=order_id, clid=client_id, orddt=order_date)

	# print(cursor.lastrowid)
	# return cursor.lastrowid
	return order_id

# Inserta un detalle de un pedido a la tabla Detalle-Pedido
def insert_order_detail(cursor, order_id):
	# Pedir al usuario los datos del detalle de pedido
	product_id, quantity = detail.get_detail_data()

	# Chequear que hay stock para el pedido con la cantidad deseada
	result = h.check_stock(cursor, product_id, quantity)
	if not result:
		print("Cancelando detalle de pedido...")
		return False

	# En caso de haber stock insertar el detalle de pedido y actualizar stock
	sql = '''
	INSERT INTO detalle_pedido VALUES (:ordid, :prodid, :quan)
	'''
	cursor.execute(sql, ordid=order_id, prodid=product_id, quan=quantity)

	sql = '''
	UPDATE stock SET cantidad = cantidad - :quan WHERE Cproducto = :prodid
	'''
	cursor.execute(sql, prodid=product_id, quan=quantity)
	return True

# Registra o da de alta un nuevo pedido
def register_order(conn, cursor):
	'''
	Schema:
		Stock(PK Cproducto, cantidad)
		Pedido(PK Cpedido, Ccliente, Fecha_pedido)
		Detalle-Pedido(FK Cpedido, FK Cproducto, Cantidad), PK(Cpedido, Cproducto)
	'''
	order_id = insert_basic_data(cursor=cursor)

	cursor.execute("SAVEPOINT insert_order")

	end_transaction = False
	option = None
	while not end_transaction:
		option = order.order_menu()
		match option:
			case ORDER_OPTION.ADD_DETAIL.value:
				if insert_order_detail(cursor, order_id): print("Se ha añadido un detalle de pedido.")
				else: print("No se ha añadido ningun detalle de pedido.")
			case ORDER_OPTION.DELETE_DETAILS.value:
				print("Borrando detalles del pedido...")
				cursor.execute("ROLLBACK TO insert_order")
			case ORDER_OPTION.CANCEL_ORDER.value:
				print("Cancelando pedido...")
				conn.rollback()
				end_transaction = True
			case ORDER_OPTION.FINISH_ORDER.value:
				print("Guardando cambios...")
				conn.commit()
				print("Hecho.")
				end_transaction = True
				