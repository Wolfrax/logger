This is a simple logger for my home environment.
Logging is done to a server (raspberry running gunicorn/flask) through http POST and stores records on a json file.

The frontend is javascript that will request data from the server, or http DELETE records.

The frontend uses jquery datatables for visualization.

A test script (test.py) is included.