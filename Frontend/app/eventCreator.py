from app import userCreator
from app import sql
import hashlib
from datetime import datetime

schedName = ""
dur = 1.0
recurFlag = 0
shared = 0
creator = ""
frequency = 0
eventID = ""
now = datetime.now() #to add randomness to hash


def createEvent(eName, duration, isRecurring):
    schedName = eName
    dur = duration
    recurFlag = isRecurring
    toHash = eName + str(dur) + str(recurFlag) + str(now)
    hashed = hashlib.md5(str.encode(toHash))
    eventID = hashed.hexdigest()
    query = "insert into event(eventID, eventName, eventDuration, eventRecurs, eventShared, eventFrequency) values (%s, %s, %s, %s, %s, %s)"
    values = (eventID, schedName, dur, recurFlag, shared, frequency)
    sql.createQuery(query, values)
    if (recurs == 0):
        query = "insert into onetime (eventID) values (%s)"
        values = eventID
        sql.createQuery(query, values)
    else:
        query = "insert into recurring (eventID) values (%s)"
        values = eventID
        sql.createQuery(query, values)
    return eventID
