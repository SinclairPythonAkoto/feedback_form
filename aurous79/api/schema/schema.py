from aurous79 import app, init_mail
from flask import jsonify


@app.route("/api/v1/schema")
@app.route("/api/v1/schema/")
def schema_api():
    return jsonify("schema api")