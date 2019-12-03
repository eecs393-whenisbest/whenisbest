from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/login')
def loginPage():
    return render_template('Login_Page.html')


@app.route('/main')
def main():
    return "Testing Frontpage"
