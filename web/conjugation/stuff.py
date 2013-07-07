import hashlib

from flask import request, session
from conjugation import app

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
