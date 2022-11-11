def get_data(cursor):
	print("\n\tTabla stock")
	print("Cproducto \t cantidad")
	print("---------------------------------")
	for row in cursor.execute("select * from stock"):
		print(f"| \t{row[0]} \t| \t{row[1]} \t|")
	print("---------------------------------\n")

	print("\t\tTabla pedido")
	print("Cpedido \t Ccliente \t fecha_pedido")
	print("---------------------------------------------------------")
	for row in cursor.execute("select * from pedido"):
		print(f"| \t{row[0]} \t| \t{row[1]} \t| \t{row[2].year}/{row[2].month}/{row[2].day} \t|")
	print("---------------------------------------------------------\n")

	print("\t\tTabla detalle_pedido")
	print("Cproducto \t Cpedido \t cantidad")
	print("-------------------------------------------------")
	for row in cursor.execute("select * from detalle_pedido"):
		print(f"| \t{row[0]} \t| \t{row[1]} \t| \t{row[2]} \t|")
	print("-------------------------------------------------\n")
