from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['MONGO_DBNAME'] = 'fr'
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

mongo = PyMongo(app)

from conjugation import views, stuff
app.jinja_env.globals['csrf_token'] = stuff.generate_csrf_token


