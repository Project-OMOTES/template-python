from newchess.adapter.api.application_controller import ApplicationController
from newchess.infrastructure.app_logging import setup_logging, LogLevel
from newchess.domain.application_configuration import (
    ApplicationConfiguration,
    read_configuration_from_dict,
)
from newchess.application.configuration import read_environment_config
from newchess.adapter.spi.database.db_connection_factory import DbConnectionFactory
from newchess.adapter.spi.database.repository_factory import RepositoryFactory
import click
import logging
import traceback

logger = logging.getLogger(__name__)


def create_app(simulation: str | None) -> ApplicationController:
    config: ApplicationConfiguration = read_configuration_from_dict(read_environment_config())

    if simulation:  # simulation UUID provided via cmdline overrides environment setting
        config.simulation_id = simulation

    db_connection_factory: DbConnectionFactory = DbConnectionFactory(config)
    repo_factory: RepositoryFactory = RepositoryFactory(db_connection_factory)
    return ApplicationController(repo_factory, config)


def start_app(loglevel: str, colors: bool, simulation: str | None) -> None:
    """NewCHESS application

    This application reads data from the database and spits out data into another
    database.  It reads the database parameters from environment variables.
    """
    try:
        setup_logging(LogLevel.parse(loglevel), colors)

        app = create_app(simulation)
        app.execute()
    except Exception as error:
        logger.error(f"Error occured: {error} at: {traceback.format_exc(limit=-1)}")
        logger.debug(traceback.format_exc())


@click.command()
@click.option("--loglevel", help="Loglevel specified by the user.", default="INFO")
@click.option("--colors/--no-colors", help="display colors in the terminal", default=True)
@click.option("--simulation", help="The UUID of the simulation to run", default=None)
def cmdline_app(loglevel: str, colors: bool, simulation: str | None) -> None:
    """NewCHESS application

    This application reads data from the database and spits out data into another
    database.  It reads the database parameters from environment variables.
    """
    start_app(loglevel, colors, simulation)


if __name__ == "__main__":
    start_app(loglevel="DEBUG", colors=True, simulation=None)
