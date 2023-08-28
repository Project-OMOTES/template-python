from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl


class EsdlModel:
    path: str
    es: esdl.EnergySystem

    def __init__(self, data: str) -> None:
        # esh = EnergySystemHandler()
        # self.es = esh.load_from_string(data)
        pass
