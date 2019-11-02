from app import userHandler
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
    schedName = eName
    dur = duration
    recurFlag = isRecurring
    toHash = eName + str(dur) + str(recurFlag) + str(now)
    hashed = hashlib.md5(str.encode(toHash))
    eventID = hashed.hexdigest()
    query = "insert into event(eventID, eventName, eventDuration, eventRecurs, eventShared, eventFrequency) values (%s, %s, %s, %s, %s, %s)"
    values = (eventID, schedName, dur, recurFlag, shared, frequency)
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
