import MySQLdb

conn = MySQLdb.connect(
                        host = '127.0.0.1',
                        port = 3306,
                        user = 'root',
                        passwd = 'DAfo4946816',
                        db = 'zym',
                        charset = 'utf8'
                        )

cursor = conn.cursor()

print conn

print cursor
