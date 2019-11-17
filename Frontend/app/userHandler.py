from app import sql
from app import emailer
from app import passHandler

def createUser(email, fName, lName, rawPass):
    hashedPass = passHandler.getHash(rawPass)
    query = "insert into Users(userID,FName,LName,Pass) values (%s,%s,%s,%s)"
    values = (email,fName,lName,hashedPass)
    sql.createQuery(query,values)

def editFirstName(fName,email):
    query = "update Users set FName = %s where userID = %s"
    values = (fName, email)
    sql.createQuery(query,values)

def editLastName(lName,email):
    query = "update Users set LName = %s where userID = %s"
    values = (lName, email)
    sql.createQuery(query,values)

def updateEmail(email,newEmail,pwd):
    if(passHandler.confirmPass(email,pwd)):
        query = "update Users set userID = %s where userID = %s"
        values = (newEmail,email)
        sql.createQuery(query,values)

def updatePassword(email,oldPass, newPass):
    if(passHandler.confirmPass(email,oldPass)):
        pwd = passHandler.getHash(newPass)      
        query = "update Users set Pass = %s where userID = %s"
        values = (email,pwd)
        sql.createQuery(query,values)

# def checkPassword(email,pwd):
