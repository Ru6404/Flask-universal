app.py
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return f"API KEY: {app.config['API_KEY']} — работает!"

if __name__ == '__main__':
    app.run(debug=True)
