from app import sql


def attendeeAccept(eventID, userName, userEmail):
    query = "insert into Responses(eventID, userName, userEmail) values (%s, %s, %s)"
    values = (eventID, userName, userEmail)
    sql.createQuery(query, values)


def getAttendeeName(userEmail, eventID):
    query = "select userName from Responses where userEmail = %s and eventID = %s"
    values = (userEmail, eventID)
    return sql.getQueryResults(query, values)


def attendeeAvailability(userEmail, eventID):
    query = "select userEmail, timeSlot from Responses where userEmail = %s and eventID = %s"
    values = (userEmail, eventID)
    return sql.getQueryResults(query, values)


def attendeeEdit(userEmail, timeList, eventID):
    # step 1: fetch auxiliary values
    uName = getAttendeeName(userEmail, eventID)[0][0]
    # step 2: remove existing entries
    query = "delete from Responses where userEmail = %s and eventID = %s"
    values = (userEmail, eventID)
    sql.createQuery(query, values)
    # step 3: add new entries from array of times
    # TODO: Implement for each loop
    return attendeeSubmit(userEmail, eventID, uName, timeList)


def attendeeSubmit(userEmail, eventID, userName, timeList):
    # Is attendee name needed?
    query = "insert into Responses(userEmail, eventID, userName, timeSlot) values (%s, %s, %s, %s)"
    for timeSlot in timeList:
        values = (userEmail, eventID, userName, timeSlot)
        sql.createQuery(query, values)
    return attendeeAvailability(userEmail, eventID)
