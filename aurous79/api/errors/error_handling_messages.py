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


# Define a custom error handler for 403 Unauthorized Access errors
@app.errorhandler(403)
def handle_unauthorized_access_error(error):
    return jsonify({'error': 'Unauthorized access'}), 403
