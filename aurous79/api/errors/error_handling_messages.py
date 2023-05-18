from typing import List, Dict
from aurous79 import app
from flask import jsonify


# Define a custom error handler for 404 Not Found errors
@app.errorhandler(404)
def handle_not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

# Define a custom error handler for 500 Internal Server Error errors
@app.errorhandler(500)
def handle_internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# create & define custom error handlers
@app.errorhandler(404)
def handle_no_feeback_form_error(error):
    """Error message to handle no feedback form in db"""
    return jsonify({"error": "Feedback form not found. The feedback form is empty."})

@app.errorhandler(404)
def handle_no_email_error(error):
    """Error message to handle no email in email library db"""
    return jsonify({"error": "No email found. The Aurous email library is empty."})

@app.errorhandler(403)
def handle_unauthorized_access_error(error):
    """Error message to handle unauthorized access to routes"""
    return jsonify({"error": "Unauthorized access."})