import os
import signal
from flask import Flask, request, jsonify
from flask_cors import CORS 
from utils.logger import Logger
from utils.load_file import select_audio_file
from utils.transcribe import get_transcribed_text
from flask_swagger_ui import get_swaggerui_blueprint
import sys

app = Flask(__name__)
CORS(app)

# get the api key
API_KEY = os.getenv('API_KEY')

# create logger instance
logger=Logger()

# for swagger documentation
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Middleware: before each request
@app.before_request
def before_request_func():
    # This will run before every request
    logger.info(f"Request from {request.remote_addr} at {request.method} {request.url}")

# Error response in case of route not found
@app.errorhandler(404)
def not_found_error(e):
    return jsonify({
        "error": True,
        "message": "URL not found"
    }), 404

# Error response in case of method not allowed
@app.errorhandler(405)
def method_not_allowed_error(e):
    return jsonify({
        "error": True,
        "message": "Method not allowed"
    }), 405

def validate_api_key():
    # Validate the API key from the request headers.
    api_key = request.headers.get('X-API-KEY')
    if api_key is None or api_key != API_KEY:
        return False
    return True

@app.route("/api/transcribe", methods=['POST'])
def complaint_detector():
    # Validate the API key
    if not validate_api_key():
        return jsonify({
            "error":True,
            "message": "Unauthorized access"
        }), 401
    try:
        # Get the image file from the request
        if 'audio_file' not in request.files:
            return jsonify({
                "error": True,
                'message': 'No file part in the request'
                }), 400

        # Get the audio file from the request
        file = request.files['audio_file']


        # Check if file exists or not
        if file.filename == '':
            return jsonify({
                "error": True,
                'message': 'No selected file'
                }), 400

        # Ask the user to select a file
        # file_path = select_audio_file()
        # Save the file locally
        os.makedirs("uploads", exist_ok=True)
        file_path = f"./uploads/{file.filename}"
        file.save(file_path)

        result = get_transcribed_text(file_path) 
        return jsonify({
            'language':result["language"],
            'transcribed_text': result["text"]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

# Graceful shutdown function
def graceful_shutdown(signal, frame):
    logger.info("Shutting down gracefully...")
    # Perform any cleanup here if needed
    sys.exit(0)

# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, graceful_shutdown)
signal.signal(signal.SIGTERM, graceful_shutdown)

# Main program
if __name__ == "__main__":
    app.run(debug=True, host = os.getenv('HOST'),port=os.getenv('PORT'))
