import os
from flask import Flask
from flask import request
import json
import requests
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Python!"


@app.route("/post", methods=["POST"])
def post():
    data = request.get_json()
    print(data)
    return data


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
