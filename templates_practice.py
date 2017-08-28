# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:58:20 2017

@author: vaibhav_kamat
"""
# This program is for introduction to templates used in bottle, which are present in the views directory
from bottle import get, post, request, route, run, template

@route('/')
@route('/<name>')
def hello(name='Vaibhav'):
    return template("Hello {{name}}!",name=name)

@get('/login') # or @route('/login')
def login():
    return template('login')

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=='Vaibhav' and password=='password':
        return template("login_response",username=username)
    else:
        return "<p>Login failed.</p>"
        
run(host='localhost', port=8080, debug=True)