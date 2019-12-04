from app import app
from flask import render_template, request, redirect, url_for, jsonify, session
from app import passHandler, userHandler, eventHandler, attendeeHandler

app.secret_key = 'sliuufjsdpigfhjawjgouridfjnsdiulidf'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('fnfe.html'), 404


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/login')
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


@app.route('/forgot-password')
def forgotPass():
    return render_template('Forgot_Password.html')
# create route for form data, extract from the request, passHandler.email


# diff between THIS
@app.route('/pwreset')
def resetWithEmail():
    return render_template('Reset_Password.html')


# and THIS
@app.route('/pwreset/<string:email>/<string:resetID>')
def resetPass(email, resetID):
    if(userHandler.checkForReset(email, resetID)):
        return render_template('Reset_Password.html')
    else:
        return redirect(url_for('home'))


@app.route('/logmein', methods=['POST'])
def lmi():
    userID = request.form['username']
    passwd = request.form['password']
    passHandler.confirmPass(userID, passwd)
    if session['userID'] == userID:
        return redirect(url_for('getMyEvents', userID=userID))
    else:
        return redirect(url_for('login'))


@app.route('/list-events/<userID>')
def getMyEvents(userID):
    if session['userID'] == userID:
        result = eventHandler.getAllEvents(userID)
        return render_template('events_list.html', result=result)
    else:
        return redirect(url_for('home'))


@app.route('/<userID>/schedule')
def scheduleEvent(userID):
    print(userID)
    return render_template("Event_Scheduler.html", userID=userID)


@app.route('/schedule-event', methods=['POST'])
def makeMyEvent():
    return


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


@app.route('/whoops')
def forgottenPassword():
    email = request.form['username']
    userHandler.requestReset(email)
    return redirect(url_for('home'))


@app.route('/index/<eventID>')
def landing(eventID):
    if 'userID' in session:
        if eventHandler.getOwner(eventID)[0][0] == session['userID']:
            result = attendeeHandler.getAllMatching(eventID)
            session['eventID'] = eventID
            return render_template('attendee_responses.html', result=result)
        else:
            return redirect(url_for('home'))
    else:
        session['eventID'] = eventID
        return render_template('Responder.html')


@app.route('/sendTimes/<time>')
def sendTimes(time):
    if 'eventID' in session:
        attendeeHandler.finalizeEvent(session['eventID'], time)
        session.pop('eventID', None)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/respond/<eventID>', methods=['POST'])
def attendeeAvailable(eventID):
    email = request.forms['email']
    eventID = session['eventID']
    name = request.forms['name']
    timeList = request.forms['timeList']
    session['attEmail'] = email
    attendeeHandler.attendeeSubmit(email, eventID, name, timeList)
    return redirect(url_for('attendeeResponses'))


@app.route('/respond/<eventID>/<attEmail>')
def attendeeResponses(eventID, attEmail):
    print(attendeeHandler.attendeeAvailability(eventID, attEmail))
    return jsonify(attendeeHandler.attendeeAvailability(eventID, attEmail))


def jsonifySingle(e):
    return jsonify(eventID=e[0], eventName=e[1], eventDuration=e[2], eventRecurs=e[3], eventShared=e[4], eventCreator=e[5], eventFrequency=e[6], eventCreationTime=e[7], eventGranularity=e[8])
