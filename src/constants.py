'''
Constantes o variables globales.
'''

import os
from enum import Enum

# Credenciales
HOST=os.getenv("ORACLE_DB_HOST")
PORT=os.getenv("ORACLE_DB_PORT")
USER=os.getenv("ORACLE_DB_USER")
PASSWD=os.getenv("ORACLE_DB_PASSWD")
DSN=os.getenv("ORACLE_DB_DNS")

# Enums
class MENU_OPTION(Enum):
	CREATE_TABLE = 1
	DROP_TABLE = 2
	REGISTER_ORDER = 3
	SHOW_TABLES = 4
	EXIT_MENU = 5

class ORDER_OPTION(Enum):
	ADD_DETAIL = 1
	DELETE_DETAILS = 2
	CANCEL_ORDER = 3
	FINISH_ORDER = 4

# Styles
HEADER = "-"*15
IN_PROMPT = "> "