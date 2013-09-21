from bottle import route, run, template
import subprocess
import webbrowser
import json
import smc

"""
@route('/hello/<name>')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)
"""
myData = {
    'herro': {
	'args': ['a'],
	'calls': ['bye'],
    },
    'bye':{}
}

@route('/')
def beginCom():
    return json.dumps(smc.getStructure())

@route('/data')
def sendLogs():
    return json.dumps(myData)


#subprocess.call('python -m webbrowser -t "localhost:8080/data"')
webbrowser.open("http://localhost:8080")
run(host='localhost', port=8080)
