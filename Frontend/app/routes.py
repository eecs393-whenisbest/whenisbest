from app import app
from app import main as wibrunner
from flask import Flask, render_template


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/main')
def main():
    return "Testing Frontpage"
