import psycopg2
from psycopg2 import OperationalError
import yaml
from psycopg2.extensions import register_adapter, AsIs


# load yml file creds:
with open("app_login.yaml", "r") as stream:
    creds = yaml.safe_load(stream)

db_connect = creds["postgres"]


def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=db_connect["dbname"],
            user=db_connect["user"],
            password=db_connect["password"],
            port=db_connect["port"],
        )
        print("Connection to PostgreSQL DB successful")

    except OperationalError as e:
        print(f"The error of '{e}' has occured")
    return connection
