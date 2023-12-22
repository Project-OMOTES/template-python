from {{cookiecutter.python_import_name}}.adapter.database.db_connection_factory import DbConnectionFactory
from {{cookiecutter.python_import_name}}.application.repositories.input_db_repository_abstract import InputDBRepositoryAbstract
from {{cookiecutter.python_import_name}}.application.repositories.output_db_repository_abstract import (
    OutputDBRepositoryAbstract,
)
from {{cookiecutter.python_import_name}}.adapter.spi.input_db_repository import InputRepositoryDb
from {{cookiecutter.python_import_name}}.adapter.api.output_db_repository import OutputRepositoryDb

import logging

logger = logging.getLogger(__name__)


class RepositoryFactory:
    db_connection_factory: DbConnectionFactory

    def __init__(self, db_connection_factory: DbConnectionFactory) -> None:
        self.db_connection_factory = db_connection_factory
        pass

    def get_input_repository(self, db_name: str) -> InputDBRepositoryAbstract:
        connection = self.db_connection_factory.get_db_connection(db_name)
        logger.debug(
            f"Started database connection: {self.db_connection_factory.config.db_host}"
            f":{self.db_connection_factory.config.db_port}"
        )
        return InputRepositoryDb(connection)

    def get_timeseries_repository(self, db_name: str) -> OutputDBRepositoryAbstract:
        connection = self.db_connection_factory.get_db_connection(db_name)
        logger.debug(
            f"Started Timeseries database connection: {self.db_connection_factory.config.db_host}"
            f":{self.db_connection_factory.config.db_port}"
        )
        return OutputRepositoryDb(connection)
