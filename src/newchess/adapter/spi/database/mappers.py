from newchess.application.mappers.db_mapper import DbMapper
from newchess.domain.simulation_configuration import SimulationConfiguration
from newchess.domain.esdl_model import EsdlModel

from newchess.adapter.spi.database.db_models import SimulationSettings, EsdlData
from uuid import UUID


class SimulationConfigurationMapper(DbMapper):
    def to_db(self, config: SimulationConfiguration) -> SimulationSettings:
        return SimulationSettings()

    def to_entity(self, model: SimulationSettings) -> SimulationConfiguration:
        return SimulationConfiguration(
            simulation_id=UUID(str(model.id)),
            name=str(model.owner),
            timestep=model.simulation_timestep,
            duration=model.simulation_duration,
        )


class EsdlDataMapper(DbMapper):
    def to_db(self, entity: EsdlModel) -> EsdlData:
        raise NotImplementedError("EsdlDataMapper.to_db()")

    def to_entity(self, model: EsdlData) -> EsdlModel:
        return EsdlModel(str(EsdlData.esdl_data))
