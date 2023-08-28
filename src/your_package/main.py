#  Copyright (c) 2023. Deltares & TNO
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Main python file for your-package containing a hello-world function."""
import argparse
from datetime import datetime, timedelta
import logging
from .app_logging import setup_logging, LogLevel

LOGGER = logging.getLogger(__name__)


def testable_function(current_time: datetime) -> datetime:
    """Testable function that returns a semi-fixed value."""
    return current_time + timedelta(hours=1)


def return_hello_world(input: str = "", user_loglevel: str = "info") -> str:
    """
    Testable function that returns a semi-fixed value.

    This function also uses the app_logging module
    """
    setup_logging(LogLevel.parse(user_loglevel))
    output = f"level=({user_loglevel}): Hello, world!"
    LOGGER.info(output)
    LOGGER.info("Hello world has been printed.")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nieuwe Warmte Nu Python template example")
    parser.add_argument("string", help="input string argument")
    args = parser.parse_args()
    print(return_hello_world(args.string))
