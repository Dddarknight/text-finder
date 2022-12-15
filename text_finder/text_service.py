from elasticsearch import Elasticsearch
from text_finder.db import get_connection_cursor_db


LIMIT = 10


class TextService:

    def __init__(self):
        self.elastic_client = Elasticsearch("http://localhost:9200")

    def collect_ids_from_elastic(self, text_to_find):
        query = {
            "query": {
                "match": {
                    "text": {
                        "query": text_to_find
                    }
                }
            }
        }
        elastic_texts = self.elastic_client.search(
            index="texts", body=query)
        hits = elastic_texts['hits']['hits']
        if not hits:
            return []
        ids = []
        ids = [str(element['_source']['id']) for element in hits]
        return ids

    def collect_texts_from_db(self, ids):
        db_connection, db_cursor = get_connection_cursor_db()
        ids_db = ', '.join(ids)
        query_find_texts = (
            "SELECT * FROM db_texts "
            f"WHERE id IN ({ids_db})"
            "ORDER BY created_date DESC "
            f"LIMIT {LIMIT};"
        )
        try:
            db_cursor.execute(query_find_texts)
            db_connection.commit()
        except Exception:
            return []
        texts = [text[0] for text in db_cursor]
        return texts
