from app import app
from flask import render_template, session, redirect, request

@app.route('/')
@app.route('/index')
def index():
    lang_code = session.get('language', 'en')
    return render_template("index.html", lang_code=lang_code)

@app.route('/setlang/<lang_code>')
def set_language(lang_code):
    session['language'] = lang_code
    return redirect(request.referrer)

@app.before_request
def set_session_language():
    if not session.get('language') or session.get('language') not in ['en', 'da', 'el']:
        session['language'] = 'en'
