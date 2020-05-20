import pymysql as mysql

db_user = "root"
db_password = "Shannara"
db_name = "whenisbest"
db_host = "localhost"
db = mysql.connect(user=db_user, password=db_password, host=db_host, db=db_name)


cursor = db.cursor()


def createQuery(query, values):
    cursor.execute(query, values)
    db.commit()
    print(cursor.rowcount, "record(s) modified.")


def getQueryResults(query, values):
    cursor.execute(query, values)
    print(cursor.rowcount, "records fetched.")
    return cursor.fetchall()
