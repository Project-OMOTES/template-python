from newchess.application.use_cases.run_simulation import RunSimulationUsecase
from newchess.domain.application_configuration import ApplicationConfiguration
from newchess.adapter.spi.database.repository_factory import RepositoryFactory
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
        # create database objects

        input_db = self.repository_factory.get_input_repository(self.configuration.input_db)
        output_db = self.repository_factory.get_timeseries_repository(
            self.configuration.timeseries_db
        )

        actor = RunSimulationUsecase(
            UUID(self.configuration.simulation_id),
            input_db,
        )
        output_timeseries = actor.execute()

        # create output presenter and feed data into db

        pass
