from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# the app here refers to the app module (sub-directory) and NOT the app variable
from app import routes
