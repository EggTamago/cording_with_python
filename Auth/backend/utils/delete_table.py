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

print("Database deleted successfully........")

#Closing the connection
conn.close()