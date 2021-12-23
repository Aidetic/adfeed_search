from search import DocumentSearch
from utils import check_secret_key

from flask import jsonify

document_search = DocumentSearch()


def search_handler(request_form: dict):
    # Check for secret key
    check_secret_key(request_form)

    keyword = request_form["keyword"]
    workspace_id = request_form["workspace_id"]

    search_result = document_search.search(
        search_phrase=keyword, workspace_id=workspace_id
    )

    return jsonify(search_result)
