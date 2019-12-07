#!/usr/bin/python
from app import app
from app import eventHandler
from app import attendeeHandler
from datetime import datetime, timedelta


def createEvent(name, duration, isRecurring, grain):
    creator = "pjh96@case.edu"
    now = datetime.now().replace(microsecond=0)
    timeArr = ()
    for i in range(0, 5):
        timeArr = timeArr + ((now + timedelta(seconds=3600) * i),)
    eventID = eventHandler.createEvent(name, duration, isRecurring, creator, grain, timeArr)
    return eventID


def getName(eventID):
    return eventHandler.getName(eventID)[0][0]


def getDuration(eventID):
    return eventHandler.getDuration(eventID)[0][0]


def getRecurring(eventID):
    return eventHandler.getRecurring(eventID)[0][0]


def getCreator(eventID):
    return eventHandler.getOwner(eventID)[0][0]


def getEventID(creator, schedName):
    return eventHandler.getEventID(creator, schedName)[0][0]


def getAttendeeName(attEmail, eventID):
    return attendeeHandler.getAttendeeName(attEmail, eventID)[0][0]


def attendeeAvailability(attEmail, eventID):
    return attendeeHandler.attendeeAvailability(eventID, attEmail)


def attendeeSubmit(attEmail, eventID, userName, timeList):
    return attendeeHandler.attendeeSubmit(attEmail, eventID, userName, timeList)[0][0]


def attendeeEdit(attEmail, eventID, timeList):
    return attendeeHandler.attendeeEdit(attEmail, eventID, timeList)[0][0]
