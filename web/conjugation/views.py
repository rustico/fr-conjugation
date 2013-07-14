# -*- coding: utf-8 -*-
from flask import request, session, render_template, redirect, url_for
from conjugation import app, mongo
from verbs import Verbs

@app.route('/conjuguer/<temp>/<mode>')
def conjugate(temp, mode):
    verb = Verbs.get_random_verb(temp, mode)
    pronouns = Verbs.get_verb_pronouns(verb['_id'])

    return render_template('conjugate.html', temp = temp, mode = mode, verb = verb['_id'], pronouns = pronouns)

@app.route('/conjuguer/<temp>/<mode>/<verb>', methods=['POST'])
def is_conjugation_correct(temp, mode, verb):
    # User input
    inflections = []
    items = sorted(request.form.items())
    for item in items:
        if 'conjugation' in item[0]: 
            inflections.append(item[1])

    is_correct, corrections = Verbs.is_conjugation_correct(temp, mode, verb, inflections)
    session['conjugation_result'] = {'is_correct': is_correct, 
                                     'corrections':corrections, 
                                     'inflections': inflections }
    return redirect(url_for('conjugation_result', temp = temp, verb = verb, mode = mode))

@app.route('/conjuguer/result/<temp>/<mode>/<verb>')
def conjugation_result(temp, mode, verb):
    is_correct = False
    result = None
    if session.has_key('conjugation_result'): 
        result = session.get('conjugation_result')

    if result and result['is_correct']:
        return render_template('conjugation_result_right.html', temp = temp, mode =  mode, verb = verb)

    pronouns = Verbs.get_verb_pronouns(verb)
    return render_template('conjugation_result_wrong.html', 
                            result = result, 
                            pronouns = pronouns, 
                            temp = temp,
                            mode =  mode,
                            verb = verb,
                            count = range(len(pronouns)))

