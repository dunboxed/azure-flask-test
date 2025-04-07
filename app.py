import os
from flask import Flask
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info('Root route accessed')
    return "<h1>Hello Azure!</h1><p>This is a minimal Flask app running on Azure App Service.</p>"

@app.route('/debug')
def debug():
    logger.info('Debug route accessed')
    return f"Environment: {os.environ}"

# This is important for local testing
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
