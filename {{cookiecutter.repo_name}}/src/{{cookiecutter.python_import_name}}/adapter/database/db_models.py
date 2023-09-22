from peewee import Model, DateField, UUIDField, FloatField, TextField, CharField


class SimulationSettings(Model):
    id = UUIDField(primary_key=True)
    created = DateField()
    simulation_timestep = FloatField()
    simulation_duration = FloatField()
    owner = CharField()


class EsdlData(Model):
    id = UUIDField(primary_key=True)
    esdl_data = TextField()


class timeseries(Model):
    simulation_id = UUIDField()
    location = CharField()
