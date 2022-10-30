'''
Programa principal.
Aqui se ejecutara el `main loop` del programa
'''

from dotenv import load_dotenv
load_dotenv()

import constants as c

import cx_Oracle

def run():
	try:
		conn = cx_Oracle.connect(
			user=c.USER,
			password=c.PASSWD,
			dsn=f"{c.HOST}:{c.PORT}/{c.DSN}",
			encoding="UTF-8"
		)
		print(conn.version)
	except Exception as e:
		raise(e)

	# Close connection
	if conn:
		conn.close()

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
