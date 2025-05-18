app.py 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет! Это твоё первое Flask-приложение."

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return f"API_KEY: {app.config['API_KEY']}"

if __name__ == "__main__":
    app.run(debug=True)
