import os
from dotenv import load_dotenv
from psycopg2.errors import DuplicateObject, InFailedSqlTransaction

from text_finder.db import get_connection_cursor_db


load_dotenv()

HOST = os.getenv('HOST')

ES_PORT = os.getenv('ES_PORT')

URL = f'http://{HOST}:{ES_PORT}/'


def create_index():
    db_connection, db_cursor = get_connection_cursor_db()
    query_create_type = (
        "CREATE TYPE texts_idx_type AS ("
        "id bigint,"
        "text text"
        ");"
    )
    try:
        db_cursor.execute(query_create_type)
        db_connection.commit()
    except DuplicateObject:
        pass
    query_create_func = (
        "CREATE FUNCTION texts_idx_func(db_texts) "
        "RETURNS texts_idx_type IMMUTABLE STRICT LANGUAGE sql AS $$ "
        "SELECT ROW ("
        "$1.id,"
        "$1.text"
        ")::texts_idx_type;"
        "$$;"
    )
    try:
        db_cursor.execute(query_create_func)
        db_connection.commit()
    except InFailedSqlTransaction:
        pass
    query_create_index = (
        "CREATE INDEX idx_text "
        "ON db_texts "
        "USING zombodb (texts_idx_func(db_texts.*)) "
        f"WITH (url='{URL}');"
    )
    try:
        db_cursor.execute(query_create_index)
        db_connection.commit()
    except InFailedSqlTransaction:
        pass
