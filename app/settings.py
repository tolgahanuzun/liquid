from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask app
app = Flask(__name__)

# Db connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
database = SQLAlchemy(app)


try:
    import settings_local
except:
    pass