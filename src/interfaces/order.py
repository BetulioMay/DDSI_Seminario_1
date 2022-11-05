
from datetime import datetime
import constants as c

def get_order_data():
	print(c.HEADER)
	# TODO: usar UUIDs o auto increment para el id del pedido
	
	# NOTE: La insercion de un codigo de pedido es solo para testear
	order_id = ''
	client_id = ''
	while order_id == '' or order_id is None:
		print("Introduzca el codigo del pedido")
		order_id = input(c.IN_PROMPT)
	while client_id == '' or client_id is None:
		print("Introduzca su codigo de cliente")
		client_id = input(c.IN_PROMPT)
	order_date = datetime.now()
	return int(order_id), client_id, order_date

def order_menu():
	print(c.HEADER)
	print("MENU PEDIDO")
	print("Selecciona una opcion:")
	print("1. Añadir detalle de producto")
	print("2. Eliminar todos los detalles de producto")
	print("3. Cancelar pedido")
	print("4. Finalizar pedido")
	return int(input(c.IN_PROMPT))