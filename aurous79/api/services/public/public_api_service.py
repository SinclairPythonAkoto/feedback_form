import os
from typing import List, Dict
from flask import request
from aurous79 import app
from aurous79.extension import SessionLocal
from aurous79.models import FeedbackForm
from aurous79.api.errors.error_handling_messages import handle_not_found_error, handle_unauthorized_access_error
from flask import jsonify
from dotenv import load_dotenv

load_dotenv()


# define list of API keys
# private key is not needed for this section of API
VALID_API_KEYS = [os.environ["PUBLIC_API_KEY"], os.environ["PRIVATE_API_KEY"]]


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
        return handle_not_found_error(404)
    data: Dict[List[FeedbackForm]] ={
        "Feedback form results": [
            {
                "Gender": val.sex,
                "Fisrt Visit": val.first_visit,
                "Return Visit": val.return_visit,
                "Tried Shisha": val.shisha,
                "Speed": val.speed,
                "Service": val.service,
                "Food Quality": val.food_quality,
            }
            for val in feedback_results
        ]
    }
    return jsonify(data), 200



# get feedback form via ID using public API key
@app.route('/api/v1/service/feedback/<int:id>', methods=['GET'])
def get_feedback_via_id(id: int):
    # Check if the API key is valid
    if 'X-Api-Key' not in request.headers or request.headers['X-Api-Key'] not in VALID_API_KEYS:
        # create no api key found 
        return handle_unauthorized_access_error(403)
    

    # Return some data
    data = {'name': 'Alice', 'email': 'alice@example.com'}
    return jsonify(data)
