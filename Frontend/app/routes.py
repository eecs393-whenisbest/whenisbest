from app import app
from flask import render_template, request, redirect
from app import userHandler


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


@app.route('/pwreset/<email>/<resetID>')
def resetPass():
    return render_template('Reset_Password.html')
