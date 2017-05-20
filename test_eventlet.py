import flask
import logging
import sys
import ssl
import threading
import newrelic.core.application
import eventlet
# put this before newrelic init and it works
eventlet.monkey_patch()

def dothing():
    #newrelic.core.application.Application('test').activate_session()
    import newrelic.packages.requests.packages.urllib3.util.ssl_ as ssl_
    ssl_.create_urllib3_context(ssl_.ssl.PROTOCOL_TLS, ssl_.ssl.CERT_REQUIRED)
    print('ran')

logging.basicConfig()
threading.Thread(target=dothing).run()
