from app import sql


def getAttendeeName(userEmail, eventID):
    query = "select userName from Responses where userEmail = %s and eventID = %s"
    values = (userEmail, eventID)
    return sql.getQueryResults(query, values)


def attendeeAvailability(userEmail, eventID):
    query = "select userEmail, timeSlot from Responses where userEmail = %s and eventID = %s"
    values = (userEmail, eventID)
    return sql.getQueryResults(query, values)


def attendeeEdit(userEmail, eventID, userName, timeList):
    # step 1: fetch auxiliary values
    # step 2: remove existing entries
    query = "delete from Responses where userEmail = %s and eventID = %s"
    values = (userEmail, eventID)
    sql.createQuery(query, values)
    # step 3: add new entries from array of times
    # TODO: Implement for each loop
    return attendeeSubmit(userEmail, eventID, userName, timeList)


def attendeeSubmit(userEmail, eventID, userName, timeList):
    # Is attendee name needed?
    query = "insert into Responses(userEmail, eventID, userName, timeSlot) values (%s, %s, %s, %s)"
    for timeSlot in timeList:
        values = (userEmail, eventID, userName, timeSlot)
        sql.createQuery(query, values)
    return attendeeAvailability(userEmail, eventID)
