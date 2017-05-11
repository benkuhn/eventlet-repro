import flask
import logging
import sys
import ssl
import threading
import newrelic.core.application

def dothing():
    newrelic.core.application.Application('test').activate_session()
    print('ran')

logging.basicConfig()
threading.Thread(target=dothing).run()

app = flask.Flask(__name__)
@app.route('/')
def hello():
    return 'Hello world'
