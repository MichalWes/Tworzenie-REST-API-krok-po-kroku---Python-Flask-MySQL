from os import name
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    # print(request.headers)
    # print(f'method: {request.method}')
    # print(f'path: {request.path}')
    # print(f'url: {request.url}')
    print(request.headers['Content-Type'])
    print(request.json)
    print(request.json['name'])
    print(request.json.get('name'))
    return "Nalej mi piwko skarbeczku"


if __name__ == '__main__':
    app.run(debug=True)
