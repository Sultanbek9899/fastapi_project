import os

POSTGRES_USER = os.getenv("POSTGRES_USER", default="service_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", default="F8uRbA95xYM6FZLj")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", default=5432)
POSTGRES_DB = os.getenv("POSTGRES_DB", default="service_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", default="127.0.0.1")

SQLALCHEMY_DB_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)