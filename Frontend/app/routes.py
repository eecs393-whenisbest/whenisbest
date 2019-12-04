from app import app
from flask import render_template, request, redirect, url_for, jsonify
from app import passHandler, userHandler, cookieHandler, eventHandler


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/login')
def loginPage():
    return render_template('Login_Page.html')


@app.route('/scheduler-login')
def schedLogin():
    return render_template('Schedule_Login_Page.html')

@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('user', ' ', max_age=60*60)
    return res

@app.route('/create-acct')
def acctCreate():
    return render_template('Create_Account.html')


@app.route('/forgot-password')
def forgotPass():
    return render_template('Forgot_Password.html')
# create route for form data, extract from the request, passHandler.email


@app.route('/pwreset/<string:email>/<string:resetID>')
def resetPass():
    return render_template('Reset_Password.html')


@app.route('/logmein', methods=['POST'])
def lmi():
    userID = request.form['username']
    passwd = request.form['password']
    passHandler.confirmPass(userID, passwd)
    if cookieHandler.loadCookie() is not None:
        redirect(url_for('getMyEvents'))
    else:
        redirect(url_for('login'))


@app.route('/favicon.ico')
def favicon():
    return '../static/favicon.ico'


@app.route('/list-events/<userID>')
def getMyEvents(userID):
    if cookieHandler.loadCookie() is not None:
        jsonify(eventHandler.getAllEvents(userID))


@app.route('/<userID>/schedule')
def scheduleEvent(userID):
    print(userID)
    return render_template("Event_Scheduler.html", userID=userID)


@app.route('/schedule-event', methods=['POST'])
def makeMyEvent():
    s = cookieHandler.loadCookie()


def jsonifySingle(e):
    return jsonify(eventID=e[0], eventName=e[1], eventDuration=e[2], eventRecurs=e[3], eventShared=e[4], eventCreator=e[5], eventFrequency=e[6], eventCreationTime=e[7], eventGranularity=e[8])
