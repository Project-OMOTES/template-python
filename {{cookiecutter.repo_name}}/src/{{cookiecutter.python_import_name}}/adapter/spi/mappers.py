from {{cookiecutter.python_import_name}}.application.mappers.db_mapper import DbMapper, DbModel, Entity
from {{cookiecutter.python_import_name}}.domain.heat_network import HeatNetwork


class EsdlPandaPipesMapper(DbMapper):
    def to_db(self, entity: Entity) -> DbModel:
        raise NotImplementedError
        pass

    def to_entity(self, model: DbModel) -> Entity:
        return HeatNetwork()
