import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Shannara",
    database = "whenisbest"
)

cursor = db.cursor()

def createQuery(query, values):
    cursor.execute(query,values)
    db.commit()
    print(cursor.rowcount, "record(s) modified.")

def getQueryResults(query, values):
    cursor.execute(query, values)
    print(cursor.rowcount, "records fetched.")
    return cursor.fetchall()
