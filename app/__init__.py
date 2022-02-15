from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# todo al darle guardar los envia a la linea 1
#from app import routes,models
