#!/usr/bin/python
from app import app
from app import sql
from app import eventHandler
from app import userHandler
from app import attendeeHandler

SchedName = "name"
dur = 1.0
recurFlag = 0
eventID = ""
creator = ""

def createEvent (name, duration, isRecurring):
    SchedName = name
    dur = getDuration
    recurFlag = isRecurring
    eventID = eventHandler.createEvent(SchedName, dur, recurFlag)
    return eventID

def getName():
    SchedName = eventHandler.getName(eventID)
    return SchedName

def getDuration():
    dur = eventHandler.getDuration(eventID)
    return dur

def getRecurring():
    recurFlag = eventHandler.getRecurring(eventID)
    return recurFlag

def getCreator():
    creator = eventHandler.getOwner(eventID)
    return creator

def getEventID():
    eventID = eventHandler.getEventID(creator, SchedName)
    return eventID

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
