'''
Programa principal.
Aqui se ejecutara el `main loop` del programa
'''

from dotenv import *

load_dotenv()

import constants as c

def run():
	print("This is my HOST:", c.HOST)

if __name__ == "__main__":
	run()