from {{cookiecutter.python_import_name}}.application.repositories.input_db_repository_abstract import InputDBRepositoryAbstract
from {{cookiecutter.python_import_name}}.domain.esdl_model import EsdlModel
from {{cookiecutter.python_import_name}}.domain.simulation_configuration import SimulationConfiguration
from {{cookiecutter.python_import_name}}.adapter.database.db_connection import DbConnection
from {{cookiecutter.python_import_name}}.adapter.database.mappers import SimulationConfigurationMapper, EsdlDataMapper
from peewee import PostgresqlDatabase
from {{cookiecutter.python_import_name}}.adapter.database.db_models import SimulationSettings, EsdlData
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
        logger.debug(f"Started database connection: {self.db_connection}")

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
