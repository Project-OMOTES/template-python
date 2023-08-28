import os
from dotenv import dotenv_values


def read_environment_config() -> dict:
    config = {
        **dotenv_values(".env.shared"),  # load shared development variables
        **dotenv_values(".env.secret"),  # load sensitive variables
        **os.environ,  # override loaded values with environment variables
    }
    return config
