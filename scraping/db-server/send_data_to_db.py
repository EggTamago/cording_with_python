#! /usr/bin/python3

# ================
# send data to db
# ================

import psycopg2

from get_data_for_db import get_actor_list


# s1 info
s1_url = 'https://s1s1s1.com/actress/'
form = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa']
#s1_list = get_actor_list(s1_url, form)

def make_insert_data(label, actor_info):
  
    insert_data = []

    for i in range(len(actor_info)):
        tuple_list = (i, label, actor_info[i])
        insert_data.append(tuple_list)

    return insert_data


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

    # 女優の数だけデータ投入
    for i in range(len(actor_info)):

        #Preparing query to create a database
        # db名に「user」は不可
        sql = '''
                INSERT INTO actors (user_id, label, actor_name)
                VALUES (%s, %s, %s);
              '''

        #Creating a database
        cursor.execute(sql, data)
        print("Database created successfully........")

    #Closing the connection
    conn.close()
    

def main():
    
    get_list = make_insert_data('s1', form)
    send_db(get_list)

if __name__ == '__main__':

    main()
     