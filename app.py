from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello Azure!</h1><p>This is a minimal Flask app running on Azure App Service.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
