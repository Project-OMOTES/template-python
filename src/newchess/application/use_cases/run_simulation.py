from newchess.application.repositories.input_db_repository_abstract import InputDBRepositoryAbstract
import pandas as pd
import logging
from uuid import UUID

logger = logging.getLogger(__name__)


class RunSimulationUsecase:
    simulation_id: UUID
    input_db: InputDBRepositoryAbstract

    def __init__(self, simulation_id: UUID, input_db: InputDBRepositoryAbstract) -> None:
        self.input_db = input_db
        self.simulation_id = simulation_id

    def execute(self) -> pd.DataFrame:
        """
        # fetch input data
        # create esdl=>pandapipes mapping
        # run simulation
        # create pandas dataframe => db mapping
        #
        # finish
        """
        settings = self.input_db.read_simulation_settings(self.simulation_id)
        esdl_data = self.input_db.get_esdl_data(self.simulation_id)

        logger.info(f"loaded Esdl data and simulation settings: \n{esdl_data}\n{settings}")

        return pd.DataFrame()