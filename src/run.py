'''
Programa principal.
Aqui se ejecutara el `main loop` del programa
'''

from dotenv import load_dotenv
load_dotenv()

import connection

def run():
	conn = connection.connect()
	connection.close_connection(conn)

if __name__ == "__main__":
	run()

	# try:
	# 	conn = pyodbc.connect(
	# 		'DRIVER={Microsoft ODBC for Oracle};'
	# 		f'Host={c.HOST};'
	# 		f'Service Name={c.DSN};'
	# 		f'User ID={c.USER};'
	# 		f'Password={c.PASSWD};'
	# 	)
	# 	print(conn)
	# 	conn.close()
	# except Exception as e:
	# 	print(f"ERROR: {e}")
	# print(pyodbc.drivers())
