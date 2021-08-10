#!/usr/bin/env python2
# -*-coding:utf-8 -*-

# ================
# delete data from db
# ================

import psycopg2

def delete_table():

    #establishing the connection
    conn = psycopg2.connect(database="mydb",
                            user='admin',
                            password='password',
                            host='192.168.30.1',
                            port= '5432')
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    # db名に「user」は不可
    sql = '''DELETE FROM actors;'''

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    #Closing the connection
    conn.close()


def main():
    delete_table()

if __name__=='__main__':
    main()

