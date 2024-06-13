# Standard Libraries
import os
from typing import Optional
from contextlib import contextmanager

# Third-party Libraries
from loguru import logger
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector.errors import DatabaseError
from mysql.connector import MySQLConnection

# Custom Modules
from configuration.env_keys import EnvKeys
from configuration.exceptions import DatabaseCredentialsError


class MySQLHandler:
    def __init__(self):
        self._connection_pool: Optional[MySQLConnectionPool] = None

    def establish_connection_pool(self) -> None:
        if self._connection_pool is None:
            self._connection_pool = self._create_connection_pool(pool_name="monday-marketplace")
        else:
            logger.warning(
                "Connection pool already established, new pool will not be created."
            )

    @contextmanager
    def get_pool_connection(self) -> MySQLConnection:
        if self._connection_pool is None:
            raise RuntimeError(
                "MySQL connection pool is empty! Please establish connection pool before interacting "
                "with MySQL database."
            )

        connection = self._connection_pool.get_connection()
        try:
            yield connection
        finally:
            connection.close()

    @staticmethod
    def _create_connection_pool(pool_name: str, pool_size=2) -> MySQLConnectionPool:
        try:
            host = os.getenv(EnvKeys.DB_HOST)
            database = os.getenv(EnvKeys.DB_NAME)
            username = os.getenv(EnvKeys.DB_USER)
            password = os.getenv(EnvKeys.DB_PASSWORD)

            new_pool = MySQLConnectionPool(
                pool_name=pool_name,
                pool_size=pool_size,
                host=host,
                database=database,
                user=username,
                password=password
            )
            return new_pool
        except DatabaseError:
            raise DatabaseCredentialsError(
                "Error while establishing MySQL connection pool. Check your credentials and try again."
            )

    def disconnect(self) -> None:
        connection = self._connection_pool.get_connection()

        if connection:
            connection.close()
            logger.info("Connection closed.")
