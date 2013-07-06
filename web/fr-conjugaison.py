# -*- coding: utf-8 -*-
import random

from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'fr-conjugaison'
app.config['JSON_AS_ASCII'] = False
app.debug = True
mongo = PyMongo(app)

# Subject pronouns: http://en.wikipedia.org/wiki/French_personal_pronouns
PRONOUNS = ['Je', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  
PRONOUNS_CONTRACTED = ['J\'', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  

@app.route('/conjuguer/<inflection>')
def conjugate(inflection):
    total_verbs = mongo.db.verbs.count()
    random_verbs = random.randrange(total_verbs - 1)
    verb = mongo.db.verbs.find({'temps.inflection':inflection}, { '_id' : 0, 'temps': 0 }).skip(random_verbs).limit(1)[0]
    verb_first_letter = verb['verbe'][0]
    pronouns = PRONOUNS_CONTRACTED if verb_first_letter in 'aeiuoh' else PRONOUNS

    return render_template('conjugate.html', inflection = inflection, verb = verb, pronouns = pronouns)

@app.route('/conjuguer/<inflection>/<verb>', methods=['POST'])
def conjugation_result(inflection, verb):
    result = mongo.db.verbs.find_one_or_404({'temps.inflection':inflection, 'verbe' : verb}, { '_id' : 0})
    for item in result['temps']:
        if item['inflection'] == inflection:
            pass


    result = False
    return render_template('conjugation_result.html', result = result)

if __name__ == '__main__':
    app.run()
