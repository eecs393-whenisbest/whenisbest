from app import sql

def attendeeAccept(eventID, userName, userEmail):
    query = "insert into responses(eventID, userName, userEmail) values (%s, %s, %s)"
    values = (eventID, userName, userEmail)
    sql.createQuery(query, values)

def getAttendeeName(userEmail, eventID):
    query = "select userName from responses where userEmail = %s and eventID = %s"
    values = (userEmail, eventID)
    return sql.getQueryResults(query, values)

def attendeeAvailability(userEmail, eventID):
    query = "select userEmail, timeSlot from responses where userName = %s and eventID = %s"
    values = (userEmail, eventID)
    return sql.getQueryResults(query, values)

def attendeeEdit(userEmail, timeList, eventID):
    #step 1: fetch auxiliary values
    uName = getAttendeeName(userEmail, eventID)[0][0]
    #step 2: remove existing entries
    query = "delete from responses where userEmail = %s and eventID = %s"
    values = (userEmail,eventID)
    sql.createQuery(query, values)
    #step 3: add new entries from array of times
    return attendeeSubmit(userEmail, eventID, timeSlot)

def attendeeSubmit(userEmail, eventID, timeList):
    query = "insert into responses(userEmail,eventID, timeSlot) values (%s, %s, %s)"
    for timeSlot in timeList:
        values = (userEmail, eventID, timeSlot)
        sql.createQuery(query, values)
    return attendeeAvailability(userEmail)
