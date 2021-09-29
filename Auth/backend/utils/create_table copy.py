import psycopg2

#establishing the connection
conn = psycopg2.connect(database="data_visualization",
                        user='admin',
                        password='password',
                        host='192.168.30.1',
                        port= '5432')
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
# db名に「user」は不可
# users tableがあれば削除
sql = '''DROP TABLE users'''
try:
    cursor.execute(sql)
except:
    print("---no user table in this database---")

sql = '''
        CREATE TABLE users(
        user_id     SERIAL PRIMARY KEY Not Null,
        name        varchar(50) Not Null,
        password    varchar(250) Not Null,
        created_at  timestamp Not Null,
        updated_at  timestamp,
        deleted_at  timestamp
        );
     '''

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()