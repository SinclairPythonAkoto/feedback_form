import os
from typing import List, Dict
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.models import FeedbackForm
from flask import jsonify


@app.route("/api/v1/service/public")
@app.route("/api/v1/service/public/")
def public_service():
    return jsonify("public services api")

# Define a custom error handler for 404 Not Found errors
@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify({'error': 'Feedback form not found'}), 404

# Define a custom error handler for 500 Internal Server Error errors
@app.errorhandler(500)
def handle_internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500



@app.route("/api/v1/service/public/feedback")
@app.route("/api/v1/service/public/feedback/")
def public_feedback_api():
    session: SessionLocal = SessionLocal()
    feedback_results: List[FeedbackForm] = session.query(FeedbackForm).all()
    if len(feedback_results) == 0:
        error_message: Dict[str] = {"error": "Message board is empty."}
        return handle_not_found_error(404)
    data: Dict[List[FeedbackForm]] = {
        "Feedback Results": [val.to_dict() for val in feedback_results]
    }
    return jsonify(data), 200