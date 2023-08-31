from abc import ABC, abstractmethod

from newchess.domain.esdl_model import EsdlModel
from uuid import UUID
import pandas as pd


class OutputDBRepositoryAbstract(ABC):
    @abstractmethod
    def store_output_esdl(self, id: UUID, esdl: EsdlModel) -> None:
        """Store modifed ESDL in database"""

    @abstractmethod
    def store_time_series(self, id: UUID, timeseries: pd.DataFrame) -> None:
        """store timeseries in database"""
