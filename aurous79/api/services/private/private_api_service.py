from aurous79 import app, init_mail
from flask import jsonify


@app.route("/api/v1/service/private")
@app.route("/api/v1/service/private/")
def private_service():
    return jsonify("private services api")