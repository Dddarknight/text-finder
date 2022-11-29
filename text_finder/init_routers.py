from text_finder.router import create_router
from text_finder.text_service import TextService


def init_routers(app, db_connection, db_cursor):
    textservice = TextService(db_connection, db_cursor)
    router = create_router(textservice)
    app.include_router(router)
