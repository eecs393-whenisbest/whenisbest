# Software Requirements Specification for: When is Best

## (Version 1.0, Revision 0)

Prepared by:
Brian Pang, Zubair Mukhi, and Patrick Hogrell
9 / 23 / 2019

## Introduction

### Purpose

This SRS details the software functional and nonfunctional requirements for the upcoming release of When is Best. This document is intended to be used by the members of the project team that will implement and verify the correct functioning of the system. Unless otherwise noted, all stated requirements are high priority and slated for release with version 1.0 with versions 0.3 and 0.7 scheduled as functional demo variants of the project.

###Project Scope and Project Features

When-Is-Best consists of a few major components - available-time setup, time entry, and final scheduling pages. The available-times setup page allows someone to create a named event with an approximate duration, block out available times, and send the survey out to attendees. The time-entry page is sent as a survey to attendees, who can see the number of people available and the percent of people who’ve responded to the event. Final scheduling is sent back to the event organizer to decide on the time during which the event occurs. Lastly, the final time is sent back to all attendees as a calendar appointment so that a final confirmation can occur. For this, we would like to include the Google Calendar API to allow for native addition of events to calendars.


##Overall Description
###Product Perspective
When is Best is a scheduling website designed to replace existing solutions for group task scheduling. Figure 1 illustrates the interaction between When is Best, Event Schedulers, and Event Attendees. This system is expected to iterate through two functional demo states (Versions 0.3 and 0.7) before a final implementation as a functional website (Version 1.0) and might be expanded with additional functionality, time permitting.

##User Classes and Characteristics
###Event Scheduler (Scheduler)
Event Schedulers are site users who want to find a good time to host events based on the feedback of Event Attendees (Attendees). All Schedulers will use the website for When is Best and we expect the vast majority (80% of users) to access the site from mobile devices. There are a large number of potential event schedulers, each of which can be expected to make and access multiple events concurrently. Event Schedulers should be able to create either a recurring or single-occurrence event with the expectation that such an event will be correctly scheduled for convenience for all parties attending the event. Schedulers will have the ability to send a calendar appointment to all Attendees that responded to their event. Schedulers can also act as Attendees for other Schedulers’ events if invited.

###Event Attendee (Attendee)
Event Attendees are site users who are expected to respond to events created by Schedulers. Attendees should clearly understand whether an event is one-time or recurring and what times are available through their responses. Every event is expected to have multiple Attendees, all of whom are expected to provide a set of available times. All Attendees will access When is Best through a website, and we expect most (90%) Attendees to interact with When is Best through a mobile device.

##Operating Environment
We will be focusing on implementing When is Best on the major browsers, with the expectation of making it mobile compatible and should time allow, implementing an mobile application version.

###OE-1: Web Interfaces
When is Best ​​shall be forward-compatible ​​with ​​the ​​following ​​Web​ ​Browsers: Google Chrome Version 76, Firefox Version 68.1.0, Safari 12.1.2, Opera 63, and Microsoft​​ Edge ​​Version​​ 40.

###OE-2: Storage Location
When is Best shall store data on a server running up-to-date versions of MySQL, JavaScript, and Python Flask.

###OE-3: Network Location and Accessibility
When is Best shall permit user access through the Internet. Account access will be created for Event Schedulers.

##Design and Implementation Constraints

###CO-1: HTML Standards
All ​​HTML ​​code ​​shall​ ​conform ​​to ​​the HTML​5 ​​standard.

###CO-2: JavaScript Standards
All JavaScript code shall conform to JavaScript Standard Style.

###CO-3: CSS Standards
All CSS code shall conform to the CSS3 standard.

###CO-4: Python Standards
All Python code shall conform to the PEP8 Python standard.

##2.5 User Documentation
###UD-1: Help Page
A help page shall be available to Event Schedulers that explains, step by step, how to create, share, and finalize an event.

###UD-2: First-time Tutorial
The first time an Event Scheduler creates an event, the help page will be displayed automatically.

###UD-3: Event Attendee Guide
All functions for event attendees will be clearly labelled.

##2.6 Assumption and Dependencies
###AS-1: Internet Connection
The user has access to a stable Internet connection.

###AS-2: Event Existence
The user intends to create an event or state and edit their availability for an event.

###AS-3: Email Address
The user has an email address to which notifications and a calendar appointment can be sent.

###DE-1: Scheduling Database
Scheduling functionality depends on the scheduling database.

##System Features
###Create Events
####Description and Priority
Users shall be able to create an event on the site with specified frequency, duration, and a range of available days or dates.
__Priority: High__

####Stimulus and Response
Stimulus:     Scheduler wishes to create event
Response:     System queries Scheduler for event name, frequency, duration, and preferred times.

Stimulus:    Scheduler creates one-time event
Response:    System queries for list of preferred dates and times.

Stimulus:    Scheduler creates recurring event
Response:    System queries for list of preferred days and times.

####List of Functions
|Event.Create | Event is created with Name, Duration, and a flag for one-time or recurring events.|
|Event.Create.OneTime| Event data is handed to the one-time event page, where Scheduler chooses all available dates and times.|
|Event.Create.Recurring | Event data is handed to the recurring event page, where Scheduler chooses repetition frequency and available days and times.|
|Event.Create.Submit |Event data is stored in the When is Best database after all information is collected on the website and generates a primary key composed of 8 alphanumeric characters.|
|Event.Create.Share | The When is Best website creates a URL from the primary key of the event and prompts the Scheduler to invite attendees via link or email.|

###Submit Availability to Events
####Description and Priority
Attendees shall be able to submit and change their availability for events.
__Priority: High__

####Stimulus and Response
Stimulus:     Attendee accesses event for the first time
Response:     System queries Attendee for their name and email address before then querying for available dates and times.

Stimulus:    Attendee accesses event for the second (or more) time.
Response:    System finds Attendee’s previous response and prompts Attendee to change their answers.

####List of Functions
|Event.Attendee.Accept | When an Attendee clicks on a link from When is Best, the site prompts them for their name and email address.|
|Event.Attendee.Availability | System prompts Attendee to provide their available times for the current event.|
|Event.Attendee.Submit | When is Best website transmits Attendee answers back to the When is Best database for storage. A confirmation message is sent to the Attendee.|
|Event.Attendee.Edit | When is Best website retrieves Attendee’s previous answers from When is Best database and prompts Attendee to change them through the Availability and Submit steps.|


###View Responses
####Description and Priority
Schedulers shall be able to access their events to see the number of Attendees who have answered, the Attendees they invited via email who have not responded, and their availability.
__Priority: High__

####Stimulus and Response
Stimulus:    Scheduler accesses event with key
Response:    System provides summary view of all attendees’ responses

####List of Functions
|Event.Scheduler.ViewResponses | When is Best displays all Attendees’ responses with names and includes a note of any attendees who received an invite and have not responded.|

###Send Scheduling Email
####Description and Priority
Users shall be able to create an event on the site with specified frequency, duration, and a range of available days or dates.

__Priority: High__

####Stimulus and Response
Stimulus: Event Scheduler confirms a time for the event.
Response: When is Best sends an email containing a calendar appointment to all responding Attendees and Scheduler.

####List of Functions
Event.Scheduler.SendEmail
 When is Best receives a confirmation message, creates a calendar appointment, and sends it to all Attendees and Scheduler. The site also provides a confirmation message when the process is complete.


###Google Calendar Integration
####Description and Priority
On creation of an event, When is Best will attempt to use the Google Calendar API to directly create an event on the Scheduler and all permitted Attendees’ calendars.
__Priority: Medium__

####Stimulus and Response
No user-supplied stimulus/response action.

####List of Functions
|Event.Scheduler.GCalAppt | When is Best will attempt to use the Google Calendar API to create a Google Calendar event that is directly shared with Attendees if so authorized. In the case that an Attendee has not authorized this function, When is Best will default to an emailed calendar appointment for that Attendee and attempt the calendar appointment for all Attendees that authorized Google Calendar.|

###Stretch Goals
####Preferred Time Designation
Attendees will be able to mark certain times as “preferred” in their responses.
Priority: Low

####Extensible API
When is Best shall have an externally accessible API to allow for event scheduling through other applications that wish to utilize the When is Best system.
__Priority: Low__

####Delete Events
When is Best shall provide Schedulers the ability to delete events after their creation.
__Priority: Medium__

####Edit Events
When is Best shall provide Schedulers the ability to edit event name and duration after its creation.
__Priority: Medium__


##External Interface Requirements
###User Interfaces
####UI-1: User Instructions
The system shall provide instructions on how to navigate each displayed HTML page, including (but not limited to) login page, user information page, event setup page, etc.

####UI-2: Event Creation
The Event Creation page shall provide the resources for a scheduler to create an event.

####UI-3: Event Scheduler Page
The Event Scheduler Page will provide the scheduler the layout of times to schedule an event along with details about the event itself.

####UI-4: Event Attendee Availability
The Event Attendee Availability Page will provide the attendees the ability to provide when they are available for the events they wish to attend.

####UI-5: Event Confirmation
The Event Confirmation Page will provide any user with a confirmation of a scheduled event along with a link to edit it. For Schedulers, it will also include the results of the attendee’s times.

###Hardware Interfaces
####H1-1: No​​ hardware ​​interfaces ​​have ​​been ​​identified as of yet.

###Software Interfaces
####SI-1: Google ​​Calendar ​​API
#####SI-1.1: Used to update the free times a scheduler or attendee has.

###Communications Interfaces
####CI-1: No​​ Communication ​​interfaces ​​have ​​been ​​identified as of yet.

##Other Nonfunctional Requirements
###Security Requirements
####E-1: Scheduler Access Control
Schedulers shall  be required to log into When is Best for all operations.

####E-2: Event Code Security
Event codes shall be reasonably difficult to guess (36^8 guesses) without provision of said code to a user.

###Performance Requirements
####PE-1: Peak User Load
We ​​will ​​be able ​​to ​​accommodate​ ​100​​ concurrent​ ​users during peak times.

####PE-2: Page Load Times
All ​​pages ​​should ​​load​​ in ​​less ​​than​ ​10 ​​seconds ​​over​ ​a ​​1 MBps ​​modem ​​connection.  

####PE-3: Expected Response Time
Responses ​​to ​​queries ​​shall ​​take​ ​no​​ longer​​ than ​​8 ​​seconds ​​to ​​load ​​on to ​​the screen ​​after ​​the​ ​user​​ submits ​​the​ ​query.

####PE-4: Confirmation Messages
The ​​system ​​shall​​ display​​ confirmation​​ messages ​​to ​​users ​​within​​ 5​​ seconds​​ after the​​ user​​ submits ​​information​​ to​​ the ​​system

###Safety Requirements
####SR-1: No safety requirements have been identified at this time.

###Software Quality Attributes
####Availability-1: Uptime
When is Best  shall be available to users 95% of the time between 5:00am and midnight local time and 90% of the time between midnight and 5:00am local time.

####Robustness-1:  Resumption of State
If the connection between the scheduler and the system or an attendee and the system is broken prior to the user finishing providing times, When is Best shall enable the user to reconnect with the system  where they left off.
