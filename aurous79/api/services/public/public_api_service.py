from aurous79 import app, init_mail
from flask import jsonify


@app.route("/api/v1/service/public")
@app.route("/api/v1/service/public/")
def public_service():
    return jsonify("public services api")