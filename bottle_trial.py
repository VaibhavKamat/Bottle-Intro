# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:04:57 2017

@author: vaibhav_kamat
"""
from bottle import Bottle, route, run, template
app = Bottle()

# If there is no instance of Bottle() created then the decorator will be only route('/hello')
# you can use @route('/object/<id:int>'), @route('/static/<path:path>'), @route('/show/<name:re:[a-z]+>') as
# well for using int, path, or a regular expression respectively.
@app.route('/')
@app.route('/<name>')
def hello(name='Vaibhav'):
    return template("Hello {{name}}!",name=name)

run(app, host='localhost', port=8080, debug=True)