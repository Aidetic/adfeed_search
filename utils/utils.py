from settings import env

from elasticsearch import Elasticsearch
import logging


def check_secret_key(request_form: dict):
    """Check sercret key in the request form to ensure safety

    Args:
        request_form (dict): Request form
    """
    if "secret_key" in request_form:
        if request_form["secret_key"] == env.API_SECRET_ID:
            logging.info("Secret key is matching")
        else:
            raise Exception("Secret key is not matching")
    else:
        raise Exception("Add secret key in the request")


class ESHandle:
    def __init__(self) -> None:
        self.es_client = Elasticsearch([env.ELASTIC_SEARCH_URL])
        if not self.es_client:
            raise ValueError("Elasticsearch connection failed. Check elasticsearch URL")
        else:
            logging.info(
                f"Elasticsearch connection established at {env.ELASTIC_SEARCH_URL}"
            )
