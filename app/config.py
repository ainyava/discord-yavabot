from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DISCORD_TOKEN: str
    PROXY: str | None = None
    COMMAND_PREFIX: str = "!"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
