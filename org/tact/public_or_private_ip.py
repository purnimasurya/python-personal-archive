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
from IPy import IP
 



def startpy(ip_input):
    ip = IP(ip_input)
    details = ip.iptype()
    #print (ip)
    print(details)


if __name__ == '__main__':
   
    ip = "8.8.8.8"
    startpy(ip)