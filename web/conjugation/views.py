# -*- coding: utf-8 -*-
from flask import request, session, render_template
from conjugation import app, mongo
from verbs import Verbs

@app.route('/conjuguer/<temp>')
def conjugate(temp):
    verb = Verbs.get_random_verb(temp)
    pronouns = Verbs.get_verb_pronouns(verb['_id'])

    return render_template('conjugate.html', temp = temp, verb = verb['_id'], pronouns = pronouns)

@app.route('/conjuguer/<temp>/<verb>', methods=['POST'])
def conjugation_result(temp, verb):
    result = Verbs.is_conjugation_correct(temp, verb, request.form)
    return render_template('conjugation_result.html', result = result)
