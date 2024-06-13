# Custom Modules
from database.mysql_handler import MySQLHandler
from database.mysql_tables.parsking import Parking
from database.mysql_tables.client import Client
from database.mysql_tables.transaction import Transaction
from database.mysql_tables.table_names import TableNames


class MySQLTables:
    def __init__(self, mysql_handler: MySQLHandler):
        self._mysql_handler = mysql_handler
        self.parking = Parking(mysql_handler)
        self.client = Client(mysql_handler)
        self.transaction = Transaction(mysql_handler)

    def create_tables(self) -> None:
        pass

    def create_parking_table(self) -> None:
        create_table_query = (
            f"CREATE TABLE IF NOT EXIST {TableNames.PARKING} "
            f"parking_id INT AUTO_INCREMENT PRIMARY KEY, "
            f"slot_number INT NOT NULL, "
            f"slot_status ENUM('free', 'taken') DEFAULT 'free', "
            f"cost DECIMAL(2, 2), "  # number with 2 digits & 2 digits after come
            f"address VARCHAR(255) NOT NULL"
        )

        with self._mysql_handler.get_pool_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()
