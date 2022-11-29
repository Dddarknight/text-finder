LIMIT = 10


class TextService:

    def __init__(self, db_connection, db_cursor):
        self.db_cursor = db_cursor
        self.db_connection = db_connection

    def find_db_texts(self, text_to_find):
        query_select = (
            "SELECT text FROM db_texts "
            f"WHERE (texts_idx_func(db_texts)) ==> '{text_to_find}'"
            "ORDER BY created_date DESC "
            f"LIMIT {LIMIT};"
        )
        self.db_cursor.execute(query_select)
        self.db_connection.commit()
        texts = [text[0] for text in self.db_cursor]
        return texts
