from functools import lru_cache
from pydantic import BaseSettings


class Config(BaseSettings):
    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_config() -> Config:
    return Config()
