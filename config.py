from os import getenv, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

DATABASE_USERNAME = getenv("POSTGRES_USER")
DATABASE_PASSWORD = getenv("POSTGRES_PASSWORD")
DATABASE_HOST = getenv("POSTGRES_HOST")
DATABASE_PORT = getenv("POSTGRES_PORT")
DATABASE_DB = getenv("POSTGRES_DB")

SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"

CLEANUP_DATA = False