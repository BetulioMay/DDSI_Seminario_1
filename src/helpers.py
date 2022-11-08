'''
Funciones de utilidad.
'''

from datetime import datetime
import os

def check_stock(cursor, product_id, quantity):
	sql = '''
	SELECT cantidad FROM stock WHERE cproducto = :prodid
	'''
	cursor.execute(sql, prodid=product_id)
	result= cursor.fetchone()
	if result is None:
		print(f">> ERROR: No se encontro un producto con codigo {product_id}.")
		return False

	avail_quantity = result[0]
	if quantity > avail_quantity:
		print(f">> ERROR: no hay suficiente stock para el producto {product_id}.")
		return False
	
	return True

if os.getenv("DEV") == "1":
	def log(message):
		log_dt = datetime.now()
		print(f"[{log_dt.year}-{log_dt.month}-{log_dt.day} {log_dt.hour}:{log_dt.minute}:{log_dt.second}]: {message}")
else:
	def log(message):
		pass
