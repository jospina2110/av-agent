from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Base de datos
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "obras_ia"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    # OpenAI
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"  # barato para el parser

    # App
    app_env: str = "development"
    debug: bool = True

    @property
    def database_url(self) -> str:
        """URL async para SQLAlchemy + asyncpg."""
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def database_url_sync(self) -> str:
        """URL sync — solo para Alembic en modo offline."""
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"


settings = Settings()
