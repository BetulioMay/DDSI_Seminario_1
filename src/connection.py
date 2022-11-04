
import constants as c
import cx_Oracle

'''
Conectar con la base de datos Oracle con las credenciales especificadas en .env.
Devuelve un objeto `connection`.
'''
def connect():
	try:
		conn = cx_Oracle.connect(
			user=c.USER,
			password=c.PASSWD,
			dsn=f'{c.HOST}/{c.DSN}',
			encoding='UTF-8'
		)
		print("Welcome!")
		print("Version:", conn.version)
	except Exception as e:
		raise(e)

	if conn:
		return conn

'''
Cierra la conexion `conn` con la BD.
'''
def close_connection(conn):
	if conn:
		print("Closing connection...")
		conn.close()

'''
Devuelve un objeto `cursor` de una conexion a BD `conn`
'''
def get_cursor(conn):
	return conn.cursor()

def close_cursor(cursor):
	if cursor:
		print("Closing cursor...")
		cursor.close()