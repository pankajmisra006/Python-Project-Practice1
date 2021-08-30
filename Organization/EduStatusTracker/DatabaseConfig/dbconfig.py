# import mysql.connector   #pip install mysql-connector-python
#
# cnx = mysql.connector.connect(user='scott', password='password',
#                               host='127.0.0.1',
#                               database='employees')
# cnx.close()
import mysql.connector
from mysql.connector import Error
from django.db import connections
from django.db.utils import OperationalError

def getconnection():
    db_conn = connections['default']
    try:
        c = db_conn.cursor()

    except OperationalError:
        connected = False
    else:
        connected = True


