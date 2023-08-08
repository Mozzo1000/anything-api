from flask import Flask
from config import Config
from commands.insert import insert_command

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(insert_command)

@app.route('/')
def index():
    return {'name': 'anything-api', 'version': '1.0'}