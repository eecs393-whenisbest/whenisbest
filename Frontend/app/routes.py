from app import app
from app import sql


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/main')
def main():
    return "aaah!"
