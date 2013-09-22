from bottle import route, run, template, static_file
import subprocess
import os
import webbrowser
import json
import smc
import realtime
from multiprocessing import Process


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

def startServer():
    run(host='localhost', port=8080)

#p1 = Process(target = startServer)
#p1.start()
#subprocess.call('python -m webbrowser -t "localhost:8080/data"')
realtime.beginRealtime()
webbrowser.open("http://localhost:8080")
run(host='localhost', port=8080)
