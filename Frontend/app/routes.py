from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/main')
def main():
    return "Testing Frontpage"
