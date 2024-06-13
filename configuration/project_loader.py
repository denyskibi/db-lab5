# Standard Libraries
import os

# Third-party Libraries
from loguru import logger
from dotenv import load_dotenv

# Custom Modules
from configuration.env_keys import EnvKeys
from configuration.exceptions import DatabaseCredentialsError


def load_and_check_envies() -> None:
    # Step #1: Load environment variables from .env file
    load_dotenv()  # Load envies from .env file

    # Step #2: Check if needed environment variables properly loaded
    _check_database_envies()  # check database envies


def _check_database_envies() -> None:
    database_credentials = {
        'host': os.getenv(EnvKeys.DB_HOST),
        'database': os.getenv(EnvKeys.DB_NAME),
        'user': os.getenv(EnvKeys.DB_USER),
        'password': os.getenv(EnvKeys.DB_PASSWORD)
    }

    if None in database_credentials.values():
        raise DatabaseCredentialsError("Incomplete MySQL credentials. Check your .env file.")
    else:
        logger.debug("MySQL credentials checked. All keys filled with values")
