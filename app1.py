from os import name
from typing import Type
from flask import Flask, request, make_response, jsonify
from werkzeug.wrappers import response
app = Flask(__name__)


@app.route("/")
def index():
    # response = jsonify([{'id': 1, 'title': 'Title'}])
    response = jsonify({'error': 'Not Found'})
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)
