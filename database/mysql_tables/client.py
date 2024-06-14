# Custom Modules
from database.mysql_handler import MySQLHandler
from database.mysql_tables.table_names import TableNames


class Client:
    def __init__(self, mysql_handler: MySQLHandler):
        self._mysql_handler = mysql_handler

    def add_client(self, mail: str, number: int, name: str, surname: str) -> None:
        sql_query = (
            f"INSERT INTO {TableNames.CLIENT} (name, surname, number, mail) "
            f"VALUES(%s, %s, %s, %s)"
        )

        with self._mysql_handler.get_pool_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(sql_query, (name, surname, number, mail))
            connection.commit()
