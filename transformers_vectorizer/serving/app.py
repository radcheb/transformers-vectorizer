# pylint: disable=invalid-name,missing-function-docstring
import os

from flask import Flask, request, jsonify

from transformers_vectorizer import from_name

app = Flask(__name__)
INITIAL_VECTORIZER_NAME = os.environ.get('VECTORIZER_NAME', 'CAMMEMBERT')
vectorizers = {INITIAL_VECTORIZER_NAME: from_name(INITIAL_VECTORIZER_NAME)}
vectorizers[INITIAL_VECTORIZER_NAME].load()


@app.route("/load/<vectorizer_name>", methods=['POST'])
def load(vectorizer_name):
    return f"Loading {vectorizer_name} Not supported yet", 404


@app.route("/vectors", methods=['GET', 'POST'])
def to_vector():
    content = request.get_json(silent=True)
    if not content or "texts" not in content:
        return jsonify({"error": f"body must contains texts list"})
    texts = content["texts"]
    vectors = vectorizers[INITIAL_VECTORIZER_NAME].to_vectors(texts)
    return jsonify({"vectors": vectors})


@app.route("/vectors/<vectorizer_name>", methods=['GET', 'POST'])
def to_vector_by_name(vectorizer_name):
    if vectorizer_name in vectorizers:
        content = request.get_json(silent=True)
        vectors = vectorizers[vectorizer_name].to_vectors(content["texts"])
        return jsonify({"vectors": vectors})
    return jsonify({"error": f"model {vectorizer_name} not found"}), 404
