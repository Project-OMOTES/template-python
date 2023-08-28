from newchess.application.mappers.db_mapper import DbMapper, DbModel, Entity
from newchess.domain.heat_network import HeatNetwork


class EsdlPandaPipesMapper(DbMapper):
    def to_db(self, entity: Entity) -> DbModel:
        raise NotImplementedError
        pass

    def to_entity(self, model: DbModel) -> Entity:
        return HeatNetwork()
