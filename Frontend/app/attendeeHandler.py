from app import sql

def attendeeAccept(eventID, userName, userEmail):
    query = "insert into responses(eventID, userName, userEmail) values (%s, %s, %s)"
    values = (eventID, userName, userEmail)
    sql.createQuery(query, values)

def getAttendeeName(userEmail):
    query = "select userName from responses where userEmail = %s"
    values = (userEmail,)
    return sql.getQueryResults(query, values)

def attendeeAvailability(userName):
    query = "select userEmail from responses where userName = %s"
    values = (userName,)
    return sql.getQueryResults(query, values)


def attendeeEdit:
