import psycopg2

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
        INSERT INTO users (user_id, first_name, last_name, age)
        VALUES (0, 'tamago', 'egg', 200);
     '''

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()