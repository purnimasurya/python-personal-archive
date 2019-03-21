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

import pickle

def startpy():


    a = {'name' : 'Purnima', 'age' : '19'}

    file_Name = "Purnima"
    # open the file for writing
    #fileObject = open(file_Name,'wb') 

    # this writes the object a to the
    # file named 'testfile'
    #pickle.dump(a,fileObject)   

    # here we close the fileObject
    #fileObject.close()
    # we open the file for reading
    fileObject = open(file_Name,'rb')  
    # load the object from the file into var b
    b = pickle.load(fileObject)  
    print(b)



if __name__ == '__main__':
    startpy() 