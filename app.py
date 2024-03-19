from flask import Flask, render_template

from api import ApiClient

app = Flask(__name__)

BACKEND_HOST = '127.0.0.1'
BACKEND_PORT = '6000'

app.config["api"] = ApiClient(f"{BACKEND_HOST}:{BACKEND_PORT}")


@app.route("/")
def home():
    api = app.config["api"]
    return "-api.sayHello: %s\n\n-api.getAll(length=10): %s\n\n-api.getStream(length=5): %s\n" % (
        api.sayHello("Gonzalo"),
        api.getAll(length=10),
        api.getStream(length=5)
    )
