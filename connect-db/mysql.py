import mysql.connector as mydb

class ConnectionMySQL():

    def __init__(self, host, port, user, password, database) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    
    # Make Connection
    def connection(self):
        conn = mydb.connect(host=self.host,
                            port=self.port,
                            user=self.user,
                            password=self.password,
                            database=self.database)
        # recconection setting
        conn.ping(reconnect=True)
        return conn

    # Make cursor
    def cursor(self):
        conn = self.connection()
        cur = conn.cursor()
        return cur
    
    # Make sql
    def sql(self):
        cur = self.cursor()

        # id, name, priceを持つテーブルを（すでにあればいったん消してから）作成
        table = 'test'
        cur.execute("DROP TABLE IF EXISTS `%s`;", table)
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS `%s` (
            `test` varchar(32)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
            """, table)

    # Close connection and cursor
    def close(self, conn, cur):
        cur.close()
        conn.close()