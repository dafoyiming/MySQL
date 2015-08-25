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

sql_insert = "insert into user (iduser,user_name,location) values(11,'k','z')"

sql_update = "update user set user_name='y' where iduser=9"

sql_delete = "delete from user where iduser<3"

try:

    cursor.execute(sql_insert)
    print cursor.rowcount

    cursor.execute(sql_update)
    print cursor.rowcount

    cursor.execute(sql_delete)
    print cursor.rowcount

    conn.commit()

except Exception as e:
    print e
    conn.rollback()

cursor.close()

conn.close()