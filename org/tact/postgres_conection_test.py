#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: purnima

Source:
    
'''

# Import necessary modules
import psycopg2 


def startpy():


    try:
        connection = psycopg2.connect(user = "stars",
                                    password = "fivestars",
                                    host = "10.0.0.6",
                                    port = "5432",
                                    database = "stars")

        cursor = connection.cursor()
        
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


if __name__ == '__main__':
    startpy()