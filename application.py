from flask import Flask
import sys
import os

app = Flask(__name__)

@app.route('/')
def hello():
    python_info = f"<p>Python {sys.version}</p>"
    env_vars = "<ul>"
    for key, value in os.environ.items():
        env_vars += f"<li>{key}: {value}</li>"
    env_vars += "</ul>"
    
    return f"""
    <h1>Hello Azure!</h1>
    <p>This is a minimal Flask app running on Azure App Service.</p>
    <h2>Python Info:</h2>
    {python_info}
    <h2>Current Directory:</h2>
    <p>{os.getcwd()}</p>
    <h2>Directory Contents:</h2>
    <p>{os.listdir('.')}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
