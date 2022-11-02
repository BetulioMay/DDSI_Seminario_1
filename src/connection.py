
import constants as c
import cx_Oracle

def connect():
	try:
		conn = cx_Oracle.connect(
			user=c.USER,
			password=c.PASSWD,
			dsn=f'{c.HOST}/{c.DSN}',
			encoding='UTF-8'
		)
		print("Connected to database!")
		print("Version:", conn.version)
	except Exception as e:
		raise(e)

	if conn:
		return conn

def close_connection(conn):
	if conn:
		conn.close()