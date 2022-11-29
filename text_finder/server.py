import uvicorn
from fastapi import FastAPI

from text_finder.db import get_connection_cursor_db
from text_finder.index import create_index
from text_finder.init_routers import init_routers


app = FastAPI()

create_index()

db_connection, db_cursor = get_connection_cursor_db()

init_routers(app, db_connection, db_cursor)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
