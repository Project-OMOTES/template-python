from {{cookiecutter.python_import_name}}.application.use_cases.run_simulation import RunSimulationUsecase
from {{cookiecutter.python_import_name}}.domain.application_configuration import ApplicationConfiguration
from {{cookiecutter.python_import_name}}.adapter.spi.database.repository_factory import RepositoryFactory
from uuid import UUID


class ApplicationController:
    repository_factory: RepositoryFactory
    configuration: ApplicationConfiguration

    def __init__(
        self, repository_factory: RepositoryFactory, configuration: ApplicationConfiguration
    ) -> None:
        self.repository_factory = repository_factory
        self.configuration = configuration
        pass

    def execute(self) -> None:
        current_uuid = UUID(self.configuration.simulation_id)
        input_db = self.repository_factory.get_input_repository(self.configuration.input_db)
        output_db = self.repository_factory.get_timeseries_repository(
            self.configuration.timeseries_db
        )
        actor = RunSimulationUsecase(current_uuid, input_db)
        output_timeseries = actor.execute()
        output_db.store_time_series(current_uuid, output_timeseries)
