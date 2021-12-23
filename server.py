from handler import search_handler

from flask import Flask, request

app = Flask("DocumentSearch")


@app.route("/search", methods=["POST"])
def search_documents():
    request_form = request.get_json(force=True)

    result = search_handler(request_form)

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
