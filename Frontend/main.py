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

def getName():
  return SchedName

def getDuration():

  return dur

def getRecurring():

  return recurFlag

def getCreator():

  return

def getEventID():

  return
