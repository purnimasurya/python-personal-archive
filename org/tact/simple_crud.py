#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: purnima

Source:
    
'''

#
#  Import necessary modules
import psycopg2  


'''
    City
        id
        name (unique)
        state
'''

def add_row():
    pass

def read_all_rows():
    try:
        connection = psycopg2.connect(user = "stars",
                                    password = "fivestars",
                                    host = "10.0.0.3",
                                    port = "5432",
                                    database = "stars")

        cursor = connection.cursor()
        
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        
        # Print PostgreSQL version
        cursor.execute("SELECT * FROM CITY;")
        records = cursor.fetchmany(5)
        #print("You are connected to - ", record,"\n")
        print (type(records))

        for row in records:
            #print(i)
            #print(type(i))
            city = row[1]
            state = row[2]
            country = row[3]
            print(city, state, country)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def read_single_row():
    try:
        connection = psycopg2.connect(user = "stars",
                                    password = "fivestars",
                                    host = "10.0.0.3",
                                    port = "5432",
                                    database = "stars")

        cursor = connection.cursor()
        
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        
        # Print PostgreSQL version
        cursor.execute("SELECT * FROM CITY;")
        records = cursor.fetchone()
        #print("You are connected to - ", record,"\n")
        print (type(records))
        print(records)
        print(records[1])
        '''
        for row in records:
            #print(i)
            #print(type(i))
            city = row[1]
            state = row[2]
            country = row[3]
            print(city, state, country)
        '''
    

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def update_row():
    pass

def delete_row():
    pass

def startpy():
    #read_all_rows()
    read_single_row()


if __name__ == '__main__':
    startpy()
