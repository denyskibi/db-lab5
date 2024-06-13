# Custom Modules
from database.mysql_handler import MySQLHandler


class Parking:
    def __init__(self, mysql_handler: MySQLHandler):
        self._mysql_handler = mysql_handler
