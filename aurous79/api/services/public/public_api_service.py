import os
from typing import List, Dict
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.models import FeedbackForm
from aurous79.api.errors.error_handling_messages import handle_not_found_error
from flask import jsonify


@app.route("/api/v1/service/public")
@app.route("/api/v1/service/public/")
def public_service():
    return jsonify("public services api")



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