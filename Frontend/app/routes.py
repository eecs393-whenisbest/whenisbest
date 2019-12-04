from app import app
from flask import render_template, request, redirect, url_for, jsonify, session
from app import passHandler, userHandler, eventHandler

app.secret_key = 'sliuufjsdpigfhjawjgouridfjnsdiulidf'


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/login')
def loginPage():
    return render_template('Login_Page.html')


@app.route('/scheduler-login')
def schedLogin():
    return render_template('Schedule_Login_Page.html')


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
    if 'userID' in session:
        return redirect(url_for('getMyEvents', userID=userID))
    else:
        return redirect(url_for('login'))


@app.route('/favicon.ico')
def favicon():
    return '../static/favicon.ico'


@app.route('/list-events/<userID>')
def getMyEvents(userID):
    if 'userID' in session:
        return jsonify(eventHandler.getAllEvents(userID))
    else:
        redirect(url_for('login'))


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


def jsonifySingle(e):
    return jsonify(eventID=e[0], eventName=e[1], eventDuration=e[2], eventRecurs=e[3], eventShared=e[4], eventCreator=e[5], eventFrequency=e[6], eventCreationTime=e[7], eventGranularity=e[8])
