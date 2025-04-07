import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello Azure!</h1><p>This is a minimal Flask app running on Azure App Service.</p>"

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
