import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Shannara",
    database = "whenisbest"
)

cursor = db.cursor()
