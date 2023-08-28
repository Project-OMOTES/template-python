from typing import Any

# from peewee import *


class DbConnection:
    db_connection: Any

    def __init__(self, db_connection: Any) -> None:
        self.db_connection = db_connection
        pass

    def get(self) -> Any:
        return self.db_connection
