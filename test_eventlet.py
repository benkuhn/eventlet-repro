import flask
import logging

# This works:
#logging.getLogger('yo').warn('hi')
# This causes a newrelic initialization error when visiting localhost:5000
# due to a RecursionError in SSL.py when
logging.warn('hi')

app = flask.Flask(__name__)
@app.route('/')
def hello():
    return 'Hello world'
