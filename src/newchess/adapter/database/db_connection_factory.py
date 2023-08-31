from newchess.domain.application_configuration import ApplicationConfiguration
from newchess.adapter.database.db_connection import DbConnection
from peewee import PostgresqlDatabase

import logging

logger = logging.getLogger(__name__)


class DbConnectionFactory:
    config: ApplicationConfiguration

    def __init__(self, config: ApplicationConfiguration) -> None:
        self.config = config
        pass

    def get_db_connection(self, db_name: str) -> DbConnection:
        logger.debug(
            f"Creating database connection for "
            f"{self.config.db_username}@{self.config.db_host}:{self.config.db_port}"
        )
        return DbConnection(
            PostgresqlDatabase(
                db_name,
                user=self.config.db_username,
                password=self.config.db_password,
                host=self.config.db_host,
                port=self.config.db_port,
            )
        )
