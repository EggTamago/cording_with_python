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
sql = '''
        CREATE TABLE TestTable (
        pageNo   integer Not Null ,
        typeName VARCHAR (250),
        count    INTEGER,
        data     TEXT,
        CONSTRAINT TestTable_pkey PRIMARY KEY (pageNo)
        );
     '''

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()
