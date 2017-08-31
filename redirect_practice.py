# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:38:13 2017

@author: vaibhav_kamat
"""
from bottle import get, post, run, route, redirect, request, template

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
        redirect("/"+username)
    else:
        return "<p>Login failed.</p>"
        
run(host='localhost', port=8080, debug=True)
