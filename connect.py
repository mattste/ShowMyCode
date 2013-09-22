from bottle import route, run, template, static_file
import subprocess
import os
import webbrowser
import json
import smc
import realtime


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
    return template('basicD3')

@route('/structure')
def setupFxns():
    return json.dumps(smc.getStructure())

@route('/data')
def sendLogs():
    return json.dumps(myData)

@route('/realtime')
def sendActions():
    return json.dumps(realtime.getActions(), cls=realtime.MyEncoder)

@route('/visuals/:path#.+#', name='static')
def static(path):
    return static_file(path, root='./visuals/')


#subprocess.call('python -m webbrowser -t "localhost:8080/data"')
webbrowser.open("http://localhost:8080")
run(host='localhost', port=8080)
