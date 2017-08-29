# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:52:22 2017

@author: vaibhav_kamat
"""
from bottle import route, run, request

@route('/query')
def querytest():
    param1 = request.query.param1
    param2 = request.query.param2
    
    return '<h1> The value of param1 = ' + param1 + ' and the value of param2 = ' + param2 + '</h1>'
    
    
if __name__ == '__main__':
    run(debug=True)
