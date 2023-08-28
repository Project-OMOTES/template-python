from dataclasses import dataclass
from dataclass_wizard import fromdict
from typing import Any
import logging

LOGGER = logging.getLogger(__name__)


@dataclass
class ApplicationConfiguration:
    db_host: str
    db_port: str
    input_db: str
    timeseries_db: str
    db_username: str
    db_password: str
    simulation_id: str


def read_configuration_from_dict(input: dict) -> ApplicationConfiguration | Any:
    """Returns an ApplicationConfiguration object from the provided dict

    This function has the typehint Any because of the 'fromdict()' method.  The object
    returned is always an ApplicationConfiguration object
    """
    try:
        return fromdict(ApplicationConfiguration, input)
    except Exception as error:
        LOGGER.error(f"Error during parsing of config variables: {error}")
        raise error
