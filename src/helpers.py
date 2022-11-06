'''
Funciones de utilidad.
'''

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