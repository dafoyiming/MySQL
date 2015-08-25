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

sql = "select * from user"

cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()

print rs

rs = cursor.fetchmany(3)

print rs

rs = cursor.fetchall()

for row in rs:
    print "iduser=%s,username=%s,location=%s" % row

cursor.close()

conn.close()