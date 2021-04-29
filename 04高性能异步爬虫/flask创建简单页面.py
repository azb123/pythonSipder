from flask import Flask
import time

app = Flask(__name__)

@app.route('/azb')
def index_azb():
    time.sleep(2)
    return 'Hello azb'

@app.route('/xx')
def index_xx():
    time.sleep(2)
    return 'Hello xx'

@app.route('/hh')
def index_hh():
    time.sleep(2)
    return 'Hello hh'

if __name__ == '__main__':
    app.run(threaded=True)