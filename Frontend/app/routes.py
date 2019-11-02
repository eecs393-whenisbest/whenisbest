from app import app


@app.route('/')
@app.route('/index')
@app.route('/main')
def index():
    return "Hello, World!"


def main():
    return "aaah!"
