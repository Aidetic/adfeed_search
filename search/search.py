import logging
import traceback

from settings import env
from utils import ESHandle


class DocumentSearch:
    def __init__(self) -> None:
        self.es_handle = ESHandle()

    def search(self, search_phrase, workspace_id):
        query = {
            "query": {
                "bool": {
                    "minimum_should_match": 1,
                    "should": {
                        "multi_match": {
                            "query": search_phrase,
                            "type": "phrase",
                            "fields": ["page_title^2", "page_text^1"],
                        }
                    },
                    "filter": [{"term": {"workspace_id": workspace_id}}],
                }
            },
            "sort": [{"uploaded_on": {"order": "desc"}}, "_score"],
        }
        results = self.es_handle.es_client.search(
            index=env.ELASTIC_SEARCH_INDEX, body=query, size=9999, request_timeout=60
        )["hits"]["hits"]
        search_results = []
        if results:
            for result in results:
                temp = {}
                temp["file_id"] = result["_source"]["file_id"]
                temp["page_id"] = result["_source"]["page_id"]
                search_results.append(temp.copy())
        return search_results
