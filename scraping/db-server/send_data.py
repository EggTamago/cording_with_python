#!/usr/bin/env python2
# -*-coding:utf-8 -*-

# ================
# send data to db
# ================

import psycopg2

from get_data import get_actor_list

# s1 info
s1_url = 'https://s1s1s1.com/actress/'
form = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa']
s1_list = get_actor_list(s1_url, form)

def insert_data(label, actor_info):
  
    data = []

    for i in range(len(actor_info)):
        tuple_list = (i, label, actor_info[i])
        data.append(tuple_list)

    return data


def send_db(actor_info):

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
    sql = '''
            INSERT INTO actors (user_id, label, actor_name)
            VALUES (%s, %s, %s);
            '''

    #Creating a database
    cursor.executemany(sql, actor_info)
    print("Database created successfully........")

    #Closing the connection
    conn.close()
    

def main():
    
    actor_info = insert_data('s1', s1_list)
    send_db(actor_info)

if __name__ == '__main__':
    main()
     