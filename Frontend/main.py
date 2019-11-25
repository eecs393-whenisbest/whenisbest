#!/usr/bin/python
from app import app
from app import sql
from app import eventHandler
from app import userHandler
from app import attendeeHandler

def createEvent (name, duration, isRecurring):
    eventID = eventHandler.createEvent(name, duration, isRecurring, "pjh96@case.edu", 0.5)
    return eventID

def getName(eventID):
    return eventHandler.getName(eventID)

def getDuration(eventID):
    return eventHandler.getDuration(eventID)

def getRecurring(eventID):
    return eventHandler.getRecurring(eventID)

def getCreator(eventID):
    return eventHandler.getOwner(eventID)

def getEventID(creator, schedName):
    return eventHandler.getEventID(creator, SchedName)

def attendeeAccept(attName, attEmail, eventID):
    return attendeeHandler.attendeeAccept(eventID, attName, attEmail)

def getAttendeeName(attEmail, eventID):
    return attendeeHandler.getAttendeeName(attEmail, eventID)

def attendeeAvailability(attEmail, eventID):
    return attendeeHandler.attendeeAvailability(eventID, attEmail)

def attendeeSubmit(attEmail, eventID, timeList):
    return attendeeHandler.attendeeSubmit(userEmail, eventID, timeList)

def attendeeEdit(attEmail, eventID, timeList):
    return attendeeHandler.attendeeEdit(attEmail, eventID, timeList)
