#!/usr/bin/python
from app import app
from app import eventHandler
from app import userHandler
from app import attendeeHandler


def createEvent(name, duration, isRecurring):
    eventID = eventHandler.createEvent(name, duration, isRecurring, "pjh96@case.edu", 0.5)
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
