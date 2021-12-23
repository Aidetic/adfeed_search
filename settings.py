import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


def check_env_varaiables(env):
    """Check if environment variables is loaded"""
    for _dir in dir(env):
        if (not _dir.startswith("__")) and (getattr(env, _dir) is None):
            print("ENV VARIABLE LOADING: FAILED!")
            raise Exception(f"{_dir} not loaded. Check .env file")
    print("ENV VARIABLE LOADING: SUCCESS!")


class EnvVariables:
    def __init__(self) -> None:
        self.ELASTIC_SEARCH_URL = os.getenv("ELASTIC_SEARCH_URL")
        self.ELASTIC_SEARCH_INDEX = os.getenv("ELASTIC_SEARCH_INDEX")
        self.API_SECRET_ID = bytes(os.getenv("API_SECRET_ID"), "utf-8").decode(
            "unicode_escape"
        )


env = EnvVariables()
check_env_varaiables(env)
