from app import sql
from app import emailer


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


def getAllMatching(eventID):
    query = "select userName, timeSlot from Responses where eventID = %s"
    values = (eventID, )
    res = sql.getQueryResults(query, values)
    temp1 = []
    for r in res:
        temp1.append(r[1])
    temp1 = list(dict.fromkeys(temp1))
    final = []
    for t in temp1:
        count = 0
        for result in res:
            if result[1] == t:
                count += 1
        final.append((t, count))
    return final


def finalizeEvent(eventID, timeSlot):
    query = "select userEmail from Responses where eventID = %s and timeSlot = %s"
    values = (eventID, timeSlot)
    results = sql.getQueryResults(query, values)
    for res in results:
        emailer.eventConfirm(res[0], timeSlot)
