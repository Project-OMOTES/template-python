from abc import ABC, abstractmethod

from newchess.domain.esdl_model import EsdlModel
from newchess.domain.simulation_configuration import SimulationConfiguration
from uuid import UUID


class InputDBRepositoryAbstract(ABC):
    @abstractmethod
    def get_esdl_data(self, id: UUID) -> EsdlModel:
        """read ESDL info from db"""

    @abstractmethod
    def read_simulation_settings(self, id: UUID) -> SimulationConfiguration:
        """read additional simulation settings"""
