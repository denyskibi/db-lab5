# Custom Modules
from database.mysql_tables import MySQLTables


class DatabaseUtils:
    def __init__(self, mysql_tables: MySQLTables):
        self._mysql_tables = mysql_tables

    def add_example_clients(self) -> None:
        self._mysql_tables.client.add_client(mail="example1@gmail.com", number=1, name="Denys", surname="K")
        self._mysql_tables.client.add_client(mail="example2@gmail.com", number=2, name="Yuri", surname="M")

    def add_example_parkings(self) -> None:
        self._mysql_tables.parking.add_parking(slot_number=1, slot_status='taken', cost=20, address="вул. Мазепи, 3")
        self._mysql_tables.parking.add_parking(slot_number=2, slot_status='taken', cost=30, address="вул. Більцька, 27")

    def add_example_transactions(self) -> None:
        self._mysql_tables.transaction.add_transaction(parking_id=1, client_id=1, payment=25, status='unpaid')
        self._mysql_tables.transaction.add_transaction(parking_id=1, client_id=2, payment=150, status='paid')
