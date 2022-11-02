#!/usr/bin/env python3

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

