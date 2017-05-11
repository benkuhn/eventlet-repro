NEW_RELIC_LICENSE_KEY=test newrelic-admin run-program gunicorn \
   test_eventlet:app -b 0.0.0.0:5000 -k eventlet
