# dev_main.py
TESTING = TRUE

import db_connection

db = db_connection.Database()

# prod_main.py
TESTING = False

import db_connection

db = db_connection.Database()

