from app import app
from flask import render_template, request, redirect, url_for, jsonify, session
from app import passHandler, userHandler, eventHandler, attendeeHandler
from datetime import datetime

app.secret_key = 'sliuufjsdpigfhjawjgouridfjnsdiulidf'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('fnfe.html'), 404

# STATIC URLs #
@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/login')
@app.route('/see-events')
def loginPage():
    if 'userID' in session:
        return redirect(url_for('getMyEvents', userID=session['userID']))
    return render_template('Login_Page.html')


@app.route('/scheduler')
def schedLogin():
    if 'userID' in session:
        return redirect(url_for('scheduleEvent', userID=session['userID']))
    else:
        return render_template('Schedule_Login_Page.html')


@app.route('/create-acct')
def acctCreate():
    return render_template('Create_Account.html')


@app.route('/event-page')
def eventButtons():
    return render_template('Event_Page.html')


@app.route('/logout')
def logout():
    if 'userID' in session:
        session.pop('userID', None)
    return redirect(url_for('loginPage'))


@app.route('/whoops', methods=['POST'])
def forgottenPassword():
    email = request.form['username']
    userHandler.requestReset(email)
    return redirect(url_for('home'))


@app.route('/forgot-password')
def forgotPass():
    return render_template('Forgot_Password.html')
    # on forgot_pass, post to reset(email)


@app.route('/pwreset')
def resetWithEmail():
    return render_template('Reset_Password.html')


# PARAMETRIC URLs #
@app.route('/pwreset/<string:email>/<string:resetID>')
def resetPass(email, resetID):
    if(userHandler.checkForReset(email, resetID)):
        return render_template('Reset_Password.html')
    else:
        return redirect(url_for('home'))


@app.route('/delete/<eventID>')
def delEvent(eventID):
    print(eventHandler.getOwner(eventID))
    if(session['userID'] == eventHandler.getOwner(eventID)[0][0]):
        eventHandler.deleteEventByID(eventID)
        return redirect(url_for('getMyEvents', userID=session['userID']))
    else:
        return(redirect('/oh-no'))


@app.route('/list-events/<userID>')
def getMyEvents(userID):
    if session['userID'] == userID:
        result = eventHandler.getAllEvents(userID)
        return render_template('events_list.html', result=result)
    else:
        return redirect('/oh-no')


@app.route('/<userID>/schedule')
def scheduleEvent(userID):
    print(userID)
    return render_template("Event_Scheduler.html", userID=userID)


@app.route('/index/<eventID>')
def landing(eventID):
    if 'userID' in session:
        if eventHandler.getOwner(eventID)[0][0] == session['userID']:
            result = eventHandler.getAllMatching(eventID)
            session['eventID'] = eventID
            if result != []:
                return render_template('attendee_responses.html', result=result)
            return redirect(url_for('emailLoader', eventID=eventID))
        else:
            return redirect(url_for('home'))
    else:
        session['eventID'] = eventID
        return redirect(url_for('fnfe'))
        # render_template()'Responder.html', eventID=eventID)


@app.route('/email/<eventID>')
def emailLoader(eventID):
    if 'userID' in session:
        if eventHandler.getOwner(eventID)[0][0] == session['userID']:
            session['eventID'] = eventID
            return render_template('Event_Invite.html')
        else:
            return(redirect(url_for('home')))
    else:
        return redirect(url_for('home'))


@app.route('/sendTimes/<time>')
def sendTimes(time):
    if 'eventID' in session:
        eventHandler.finalizeEvent(session['eventID'], time)
        session.pop('eventID', None)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/respond/<eventID>/<attEmail>')
def attendeeResponses(eventID, attEmail):
    session['eventID'] = eventID
    if eventID == session['eventID']:
        return render_template('my_response.html', result=attendeeHandler.attendeeAvailability(attEmail, eventID))
    else:
        return redirect(url_for('home'))


# POST REQUESTS #
@app.route('/logmein', methods=['POST'])
def lmi():
    userID = request.form['username']
    passwd = request.form['password']
    passHandler.confirmPass(userID, passwd)
    if session['userID'] == userID:
        return redirect(url_for('home', userID=userID))
    else:
        return redirect(url_for('loginPage'))


@app.route('/emailme', methods=['POST'])
def sendInvite():
    eventID = session['eventID']
    resp = request.form.get('Recipients')
    resp = resp.replace(" ", "")
    list = resp.split(",")
    eventHandler.shareEvent(eventID, list)
    return redirect(url_for('home'))


@app.route('/schedule-event', methods=['POST'])
def makeMyEvent():
    eventName = request.form.get('event-name')
    # startDate = request.form.getlist('Start-Date')
    # endDate = request.form.getlist('End-Date')
    # startTime = request.form.getlist('Start-Time')
    # endTime = request.form.getlist('End-Time')
    eventType = request.form.get('event-type')
    increment = float(request.form.getlist('increments')[0])
    runtime = float(request.form.get('myRange'))
    offset = 1
    if eventType == 'one-time':
        offset = 0
    timeList = []
    if(len(request.form.getlist('a')) < 2):
        times = request.form.get('a')
        t = int(times) / 1000
        timeList.append(datetime.fromtimestamp(t))
    else:
        times = request.form.getlist('a')
        for t in times:
            temp = int(t) / 1000
            timeList.append(datetime.fromtimestamp(temp))
        eventHandler.createEvent(eventName, runtime, offset, session['userID'], increment, timeList)
    return redirect(url_for('getMyEvents', userID=session['userID']))


@app.route('/create-user', methods=['POST'])
def createUser():
    fName = request.form['FirstName']
    lName = request.form['LastName']
    uName = request.form['username']
    passwd = request.form['password']
    result = userHandler.createUser(uName, fName, lName, passwd)
    if(result):
        return redirect(url_for('loginPage'))
    else:
        return "User Already Exists"


# PARAMETRIC POST #
@app.route('/respond/<eventID>', methods=['POST'])
def attendeeAvailable(eventID):
    email = request.forms['email']
    session['eventID'] = eventID
    name = request.forms['name']
    timeList = request.forms['timeList']
    session['attEmail'] = email
    attendeeHandler.attendeeSubmit(email, eventID, name, timeList)
    return redirect(url_for('attendeeResponses'))


def jsonifySingle(e):
    return jsonify(eventID=e[0], eventName=e[1], eventDuration=e[2], eventRecurs=e[3], eventShared=e[4], eventCreator=e[5], eventFrequency=e[6], eventCreationTime=e[7], eventGranularity=e[8])
