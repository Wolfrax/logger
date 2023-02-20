from flask import Flask, request, render_template, abort
import json


app = Flask(__name__)
FN = "/home/pi/app/logger/logger.json"
DB = {'data': []}


class ReverseProxied(object):
    def __init__(self, app, script_name):
        self.app = app
        self.script_name = script_name

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = self.script_name
        return self.app(environ, start_response)


app.wsgi_app = ReverseProxied(app.wsgi_app, script_name='/logger')


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


@app.route('/log', methods=['GET', 'POST', 'DELETE'])
def log():
    if request.method == 'POST':
        log = {'msg': request.form['msg'],
               'pathname': request.form['pathname'],
               'created': request.form['created'],
               'levelname': request.form['levelname']}
        DB['data'].insert(0, log)

        with open(FN, "w") as f:
            json.dump(DB, f, indent=4)
        return ""
    elif request.method == 'GET':
        return DB
    elif request.method == 'DELETE':
        data = dict(request.form)
        if data in DB['data']:
            DB['data'].remove(data)
            with open(FN, "w") as f:
                json.dump(DB, f, indent=4)
            return DB
        else:
            abort(404)
    else:
        abort(400)


try:
    with open(FN, "r") as f:
        DB = json.load(f)
except json.decoder.JSONDecodeError:
    pass  # File exists but is empty
except FileNotFoundError:
    pass
