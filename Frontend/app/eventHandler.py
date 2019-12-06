from app import sql
import hashlib
from datetime import datetime
from app import emailer

schedName = ""
dur = 1.0
recurFlag = 0
shared = 0
creator = ""
frequency = 0
eventID = ""
now = datetime.now()  # to add randomness to hash


def createEvent(eName, duration, isRecurring, creator, grain, timeList):
    now = datetime.now()
    schedName = eName
    dur = duration
    recurFlag = isRecurring
    toHash = eName + str(dur) + str(recurFlag) + str(now)
    hashed = hashlib.md5(str.encode(toHash))
    eventID = hashed.hexdigest()
    query = "insert into Event(eventID, eventName, eventDuration, eventRecurs, eventShared, eventFrequency, eventCreator, eventCreationTime, eventGranularity) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (eventID, schedName, dur, recurFlag, shared, frequency, creator, now, grain)
    sql.createQuery(query, values)
    if (recurFlag == 1):
        for t in timeList:
            query = "insert into Recurring (eventID, day, timeSlot) values (%s, %s, %s)"
            values = (eventID, t.weekday(), t.time())
            sql.createQuery(query, values)
    else:
        for t in timeList:
            query = "insert into OneTime (eventID, date, timeSlot) values (%s, %s, %s)"
            values = (eventID, t.date(), t.time())
            sql.createQuery(query, values)
    return eventID


def getName(eventID):
    query = "select eventName from Event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records


def getDuration(eventID):
    query = "select eventDuration from Event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records


def getRecurring(eventID):
    query = "select eventRecurs from Event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records


def getOwner(eventID):
    query = "select eventCreator from Event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records


def getEventID(eventCreator, eventName):  # TODO: formatting for datetime
    query = "select eventID, eventCreationTime from Event where eventName=%s and eventCreator=%s"
    values = (eventName, eventCreator)
    records = sql.getQueryResults(query, values)
    return records


def deleteEventByID(eventID):
    query = "delete from Event where eventID=%s"
    values = (eventID,)
    sql.createQuery(query, values)


def deleteEventByCreator(eventCreator):
    query = "delete from Event where eventCreator=%s"
    values = (eventCreator, )
    sql.createQuery(query, values)


def getAllDetails(eventID):
    query = "select * from Event where eventID = %s"
    values = (eventID,)
    return sql.getQueryResults(query, values)


def shareEvent(eventID, emailList):
    for address in emailList:
        emailer.emailEvent(address, eventID)


def getAllEvents(userID):
    query = "select * from Event where eventCreator = %s"
    values = (userID, )
    return sql.getQueryResults(query, values)


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
    query = "delete from Responses where eventID = %s and timeSlot !=%s"
    values = (eventID, timeSlot)
    sql.createQuery(query, values)


def getAllResponses(eventID):
    query = "select userName, timeSlot from Responses where eventID = %s"
    values = (eventID, )
    return sql.getQueryResults(query, values)
