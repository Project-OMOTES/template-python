from {{cookiecutter.python_import_name}}.application.mappers.db_mapper import DbMapper
from {{cookiecutter.python_import_name}}.domain.simulation_configuration import SimulationConfiguration
from {{cookiecutter.python_import_name}}.domain.esdl_model import EsdlModel

from {{cookiecutter.python_import_name}}.adapter.database.db_models import SimulationSettings, EsdlData, timeseries
from uuid import UUID
import pandas as pd


class SimulationConfigurationMapper(DbMapper):
    def to_db(self, config: SimulationConfiguration) -> SimulationSettings:
        raise NotImplementedError("SimulationConfigurationMapper.to_db()")

    def to_entity(self, model: SimulationSettings) -> SimulationConfiguration:
        return SimulationConfiguration(
            simulation_id=UUID(str(model.id)),
            name=str(model.owner),
            timestep=model.simulation_timestep,
            duration=model.simulation_duration,
        )


class EsdlDataMapper(DbMapper):
    def to_db(self, entity: EsdlModel) -> EsdlData:
        return EsdlData(esdl_data=entity.to_string())

    def to_entity(self, model: EsdlData) -> EsdlModel:
        return EsdlModel(str(EsdlData.esdl_data))


class TimeseriesMapper(DbMapper):
    def to_db(self, entity: pd.DataFrame) -> timeseries:
        return timeseries()

    def to_entity(self, model: EsdlData) -> EsdlModel:
        raise NotImplementedError("TimeseriesMapper.to_entity()")
