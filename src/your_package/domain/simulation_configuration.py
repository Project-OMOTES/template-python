from newchess.domain.base_configuration_entity import BaseConfigurationEntity
from dataclasses import dataclass
import uuid


@dataclass
class SimulationConfiguration(BaseConfigurationEntity):
    simulation_id: uuid.UUID
    name: str
    timestep: float
    duration: float
