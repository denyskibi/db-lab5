# Standard Libraries
from typing import Literal

# Custom Modules
from database.mysql_handler import MySQLHandler
from database.mysql_tables.table_names import TableNames


class Transaction:
    def __init__(self, mysql_handler: MySQLHandler):
        self._mysql_handler = mysql_handler

    def add_transaction(self, parking_id: int, client_id: int, payment: float, status: Literal['unpaid', 'paid']) -> None:
        sql_query = (
            f"INSERT INTO {TableNames.TRANSACTION} (parking_id, client_id, payment, status) "
            f"VALUES (%s, %s, %s, %s)"
        )

        with self._mysql_handler.get_pool_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_query, (parking_id, client_id, payment, status))
            connection.commit()
