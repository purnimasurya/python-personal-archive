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
 
import xlrd


def startpy():
    loc = "Sample.numbers" 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    #print(sheet.cell_value(0,0))
    #print(sheet.nrows)
    
    
    for i in range (sheet.nrows):
        #print (sheet.row(i))
        #for j in range (sheet.ncols):
            
         print (sheet.row_values(i))
         
         
         


if __name__ == '__main__':
    startpy()