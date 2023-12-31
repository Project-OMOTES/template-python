from {{cookiecutter.python_import_name}}.application.repositories.output_db_repository_abstract import (
    OutputDBRepositoryAbstract,
)
from {{cookiecutter.python_import_name}}.domain.esdl_model import EsdlModel
from {{cookiecutter.python_import_name}}.adapter.database.db_connection import DbConnection
from {{cookiecutter.python_import_name}}.adapter.database.mappers import (
    EsdlDataMapper,
    TimeseriesMapper,
)
from peewee import PostgresqlDatabase
from {{cookiecutter.python_import_name}}.adapter.database.db_models import EsdlData, timeseries
from uuid import UUID
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class OutputRepositoryDb(OutputDBRepositoryAbstract):
    db_connection: PostgresqlDatabase

    def __init__(self, db_connection: DbConnection) -> None:
        super().__init__()
        self.db_connection = db_connection.get()
        self.db_connection.bind([EsdlData, timeseries])
        self.timeseries_mapper = TimeseriesMapper()
        self.esdl_data_mapper = EsdlDataMapper()

    def store_output_esdl(self, id: UUID, esdl: EsdlModel) -> None:
        """Store modifed ESDL in database"""
        db_data = self.esdl_data_mapper.to_db(esdl)
        db_data.save()
        raise NotImplementedError("OutputRepositoryDb.store_output_esdl")

    def store_time_series(self, id: UUID, timeseries_data: pd.DataFrame) -> None:
        logger.info("storing timeseries into database")
        db_data = self.timeseries_mapper.to_db(timeseries_data)
        db_data.save()
        """store timeseries in database"""
