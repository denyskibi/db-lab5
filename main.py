# Standard Libraries
import sys

# Third-party Libraries
from loguru import logger

# Custom Modules
from configuration import project_loader
from database.mysql_handler import MySQLHandler


def init():
    logger.info("Project initialization started.")

    # Step #1: Configurate console logging (primitive variation without a config)
    #   DEBUG - you will see all messages including debug (good for dev runs, debug, running in background on server)
    #   INFO - you will see only the main info during project workflow (good for functional runs)
    logger.remove()  # reset current logger
    logger.add(sys.stderr, level="INFO")  # create new logger & set log level

    # Step #1: Load and check project envies
    project_loader.load_and_check_envies()

    logger.success("Project initialization finished.")


def stop():
    sys.exit(1)


def main() -> None:
    # Create necessary class instances
    mysql_handler = MySQLHandler()

    try:
        # Step #1: Initialize project
        init()

        # Step #2: Establish connections
        mysql_handler.establish_connection_pool()

        # Step #3: Initialize MySQL database
        ...
    except KeyboardInterrupt:
        logger.error(f'Failed: script interrupted by user (CTRL + C)')
        stop()
    except Exception as e:
        logger.exception(f'Failed due to unexpected error: {e}', e)
    else:
        logger.success('Script finished without any critical errors.')


if __name__ == '__main__':
    main()
