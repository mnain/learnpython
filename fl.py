import time
from flask import Flask
app = Flask(__name__)

@app.route('/now')
def index():
    return 'Now '+time.strftime("%H:%M:%S")

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
