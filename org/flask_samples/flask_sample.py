#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: Purnima
Source:
    
'''

# Import necessary modules
 
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hey there!!"

if __name__ == '__main__':
    app.run()
