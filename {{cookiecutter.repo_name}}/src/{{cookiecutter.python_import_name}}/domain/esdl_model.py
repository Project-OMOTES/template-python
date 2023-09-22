from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl


class EsdlModel:
    path: str
    esh: EnergySystemHandler
    es: esdl.EnergySystem

    def __init__(self, data: str) -> None:
        # self.esh = EnergySystemHandler()
        # self.es = self.esh.load_from_string(data)
        pass

    def to_string(self) -> str:
        # return self.esh.to_string()
        return ""
