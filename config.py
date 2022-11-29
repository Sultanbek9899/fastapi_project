import os

POSTGRES_USER = os.getenv("POSTGRES_USER", default="postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", default="")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", default=5432)
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", default="service_db")

