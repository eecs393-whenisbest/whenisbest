#!/usr/bin/python
from app import app
from app import sql
from app import eventCreator
from app import userCreator

SchedName = "name"
dur = 1.0
recurFlag = 0

def createEvent (name, duration, isRecurring):
    eventCreator.createEvent(name, duration, isRecurring)

   query = "INSERT INTO "



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
