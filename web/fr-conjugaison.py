# -*- coding: utf-8 -*-
import random
import hashlib

from flask import Flask, request, session, render_template, abort
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'fr'
app.config['JSON_AS_ASCII'] = False
app.debug = True
mongo = PyMongo(app)

# Subject pronouns: http://en.wikipedia.org/wiki/French_personal_pronouns
PRONOUNS = ['Je', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  
PRONOUNS_CONTRACTED = ['J\'', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  

@app.route('/conjuguer/<temp>')
def conjugate(temp):
    total_verbs = mongo.db.verbs.count()
    random_verbs = random.randrange(total_verbs - 1)
    verb = mongo.db.verbs.find({'temps.' + temp: {'$exists': True } }).skip(random_verbs).limit(1)[0]
    first_letter = verb['_id'][0]
    pronouns = PRONOUNS_CONTRACTED if first_letter in 'aeiuoh' else PRONOUNS

    return render_template('conjugate.html', temp = temp, verb = verb['_id'], pronouns = pronouns)

@app.route('/conjuguer/<temp>/<verb>', methods=['POST'])
def conjugation_result(temp, verb):
    verb = mongo.db.verbs.find_one_or_404({'_id' : verb})
    result = False
    return render_template('conjugation_result.html', result = result)


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = csrf_token()
    return session['_csrf_token']

def csrf_token():
    return hashlib.md5().hexdigest()

app.jinja_env.globals['csrf_token'] = generate_csrf_token
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run()
