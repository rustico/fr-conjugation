# -*- coding: utf-8 -*-
from flask import request, session, render_template
from conjugation import app, mongo
from verbs import Verbs

@app.route('/conjuguer/<temp>/<mode>')
def conjugate(temp, mode):
    verb = Verbs.get_random_verb(temp, mode)
    pronouns = Verbs.get_verb_pronouns(verb['_id'])

    return render_template('conjugate.html', temp = temp, mode = mode, verb = verb['_id'], pronouns = pronouns)

@app.route('/conjuguer/<temp>/<mode>/<verb>', methods=['POST'])
def conjugation_result(temp, mode, verb):
    # User input
    inflections = []
    items = sorted(request.form.items())
    for item in items:
        if 'conjugation' in item[0]: 
            inflections.append(item[1])

    is_correct, corrections = Verbs.is_conjugation_correct(temp, mode, verb, inflections)
    return render_template('conjugation_result.html', result = result)
