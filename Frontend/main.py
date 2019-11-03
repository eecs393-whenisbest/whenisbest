#!/usr/bin/python
from app import app
from app import sql
from app import eventHandler
from app import userHandler

SchedName = "name"
dur = 1.0
recurFlag = 0
eventID = ""

def createEvent (name, duration, isRecurring):
    eventID = eventHandler.createEvent(name, duration, isRecurring)
    return eventID

def getName(eventID):
    return eventHandler.getName(eventID)

def getDuration():
    return eventHandler.getDuration(eventID)

def getRecurring():
    return eventHandler.getRecurring(eventID)

def getCreator():
    return eventHandler.getOwner(eventID)

def getEventID():
    return eventHandler.getEventID(eventCreator, eventName)
