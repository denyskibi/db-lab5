# Standard Libraries
from typing import Literal

# Custom Modules
from database.mysql_handler import MySQLHandler
from database.mysql_tables.table_names import TableNames


class Parking:
    def __init__(self, mysql_handler: MySQLHandler):
        self._mysql_handler = mysql_handler

    def add_parking(self, slot_number: int, slot_status: Literal['free', 'taken'], cost: float, address: str) -> None:
        sql_query = (
            f"INSERT INTO {TableNames.CLIENT} (slot_number, slot_status, cost, address) "
            f"VALUES(%s, %s, %s, %s)"
        )

        with self._mysql_handler.get_pool_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_query, (slot_number, slot_status, cost, address))
            connection.commit()
