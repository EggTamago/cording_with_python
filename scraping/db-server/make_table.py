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
        CREATE TABLE actors (
        user_id      integer Not Null,
        label        VARCHAR (250),
        actor_name    VARCHAR (250),
        CONSTRAINT actors_pkey PRIMARY KEY (user_id)
        );
     '''

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()
