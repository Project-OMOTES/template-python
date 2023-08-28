from newchess.application.repositories.input_db_repository_abstract import InputDBRepositoryAbstract
from newchess.domain.esdl_model import EsdlModel
from newchess.domain.simulation_configuration import SimulationConfiguration
from newchess.adapter.spi.database.db_connection import DbConnection
from newchess.adapter.spi.database.mappers import SimulationConfigurationMapper, EsdlDataMapper
from peewee import PostgresqlDatabase
from newchess.adapter.spi.database.db_models import SimulationSettings, EsdlData
from uuid import UUID
import logging

logger = logging.getLogger(__name__)


class InputRepositoryDb(InputDBRepositoryAbstract):
    db_connection: PostgresqlDatabase

    def __init__(self, db_connection: DbConnection) -> None:
        super().__init__()
        self.db_connection = db_connection.get()
        self.db_connection.bind([SimulationSettings, EsdlData])
        self.simconfig_mapper = SimulationConfigurationMapper()
        self.esdl_data_mapper = EsdlDataMapper()

    def get_esdl_data(self, id: UUID) -> EsdlModel:
        """read ESDL info from db"""

        data = EsdlData.select().where(EsdlData.id == id).get()
        logger.debug(f"Got EsdlData: {data}")
        return self.esdl_data_mapper.to_entity(data)

    def read_simulation_settings(self, id: UUID) -> SimulationConfiguration:
        """read additional simulation settings"""
        data = SimulationSettings.select().where(SimulationSettings.id == id).get()
        logger.debug(f"Got SimulationSettings: {data}")

        return self.simconfig_mapper.to_entity(data)
