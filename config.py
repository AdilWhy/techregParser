from os import getenv, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

DATABASE_USERNAME = getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = getenv("DATABASE_PASSWORD")
DATABASE_HOST = getenv("DATABASE_HOST")
DATABASE_PORT = getenv("DATABASE_PORT")
DATABASE_TABLE = getenv("DATABASE_TABLE")
DATABASE_CERT_FILE = getenv("DATABASE_CERT_FILE")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_TABLE}?ssl_ca={DATABASE_CERT_FILE}"

CLEANUP_DATA = False