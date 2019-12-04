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


@app.route('/create-acct')
def acctCreate():
    return render_template('Create_Account.html')


@app.route('/forgot-password')
def forgotPass():
    return render_template('Forgot_Password.html')


@app.route('/pwreset/<string:email>/<string:resetID>')
def resetPass():
    return render_template('Reset_Password.html')


@app.route('/logmein', methods=['POST'])
def lmi():
    userID = request.args.get('username')
    passwd = request.args.get('password')
    passHandler.confirmPass(userID, passwd)
    if cookieHandler.loadCookie is not None:
        redirect(url_for('getMyEvents'))
    else:
        redirect(url_for('login'))


@app.route('/favicon.ico')
def favicon():
    return '../static/favicon.ico'


@app.route('/list-events/<UserID>')
def getMyEvents(userID):
    if cookieHandler.loadCookie is not None:
        jsonify(eventHandler.getAllEvents(userID))
