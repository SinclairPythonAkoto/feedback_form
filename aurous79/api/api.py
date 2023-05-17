from aurous79 import app, init_mail


@app.route('/api')
def index():
    return "Hello, World!"