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

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.reckontalk.com/cricket-players-date-of-birth/')
page = requests.get('http://www.espncricinfo.com/india/content/player/30045.html')
soup = BeautifulSoup(page.text, 'html.parser')    

def is_month(content):
    content = content.lower()
    if ('july' in content):
        return True
    if ('june' in content):
        return True
    return False 

div_tags = soup.select("div.panel panel-primary td")
div_tags = soup.select("div p.ciPlayerinformationtxt")

print(div_tags)
#print(div_tags)

for dts in div_tags:
    print(dts.text)
    if (is_month(dts.text)):
        print(dts.text)