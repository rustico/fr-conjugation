# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify, json
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'fr-conjugaison'
app.config['JSON_AS_ASCII'] = False
app.debug = True
mongo = PyMongo(app)

@app.route('/conjuguer/<verb>')
def conjugate(verb):
    verb = mongo.db.verbs.find_one({'verbe':verb}, { '_id' : 0, 'verbe': 0})
    return jsonify(verb)

if __name__ == '__main__':
    app.run()
