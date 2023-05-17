from aurous79 import app, init_mail
from flask import jsonify


@app.route("/api/v1")
@app.route("/api/v1/")
def models_api():
    return jsonify("This will be the documentation of the api")