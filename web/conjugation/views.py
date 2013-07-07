# -*- coding: utf-8 -*-
import random

from flask import request, session, render_template
from conjugation import app, mongo

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
