from aurous79 import app, init_mail
from flask import jsonify


@app.route("/api/v1/route")
@app.route("/api/v1/route/")
def route_api():
    return jsonify("routes api")