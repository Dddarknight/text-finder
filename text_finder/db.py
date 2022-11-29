import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


DB = os.getenv('POSTGRES_DB')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('POSTGRES_PORT')


def get_connection_cursor_db():
    connection = psycopg2.connect(
        dbname=DB,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
    )
    cursor = connection.cursor()
    return connection, cursor
