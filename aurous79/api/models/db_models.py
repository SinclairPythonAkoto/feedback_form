from aurous79 import app, init_mail
from flask import jsonify

@app.route("/api/v1/models")
@app.route("/api/v1/models/")
def db_models():
    return jsonify("models api")