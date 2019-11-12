from app import sql
import hashlib
from datetime import datetime
from datetime import date

schedName = ""
dur = 1.0
recurFlag = 0
shared = 0
creator = ""
frequency = 0
eventID = ""
now = datetime.now() #to add randomness to hash


def createEvent(eName, duration, isRecurring):
    now = datetime.now()
    schedName = eName
    dur = duration
    recurFlag = isRecurring
    toHash = eName + str(dur) + str(recurFlag) + str(now)
    hashed = hashlib.md5(str.encode(toHash))
    eventID = hashed.hexdigest()
    query = "insert into event(eventID, eventName, eventDuration, eventRecurs, eventShared, eventFrequency, eventCreator, eventCreationTime) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (eventID, schedName, dur, recurFlag, shared, frequency, "pjh96@case.edu", now)
    sql.createQuery(query, values)
    if (recurFlag == 1):
        query = "insert into recurring (eventID, day, timeSlot) values (%s, %s, %s)"
        values = (eventID, 1, 0.25)
        sql.createQuery(query, values)
    else:
        query = "insert into onetime (eventID, date, timeSlot) values (%s, %s, %s)"
        values = (eventID, date.today(), 0.25)
        sql.createQuery(query, values)
    return eventID

def getName(eventID):
    query = "select eventName from event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records

def getDuration(eventID):
    query = "select eventDuration from event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records

def getRecurring(eventID):
    query = "select eventRecurs from event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records

def getOwner(eventID):
    query = "select eventCreator from event where eventID=%s"
    values = (eventID,)
    records = sql.getQueryResults(query, values)
    return records

def getEventID(eventCreator, eventName): #TODO: formatting for datetime
    query = "select eventID, eventCreationTime from event where eventName=%s and eventCreator=%s"
    values = (eventName, eventCreator)
    records = sql.getQueryResults(query, values)
    return records

def deleteEventByID(eventID):
    query = "delete from event where eventID=%s"
    values = (eventID,)
    sql.createQuery(query, values)

def deleteEventByCreator(eventCreator):
    query = "delete from event where eventCreator=%s"
    values = (eventCreator, )
    sql.createQuery(query, values)

def getAllDetails(eventID):
    query = "select * from event where eventID = %s"
    values = (eventID,)
    return sql.getQueryResults(query,values)
