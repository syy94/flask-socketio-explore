from flask import Flask, render_template, request
from flask_socketio import send, emit, SocketIO, join_room, leave_room
import threading
import eventlet

# change all python threading to eventlet friendly
eventlet.monkey_patch()

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

latest = None

@app.route('/')
def index():
    return 'Index Page'

@socketio.on('connect')
def test_connect():
	global latest

	user = request.sid
	print("%s connected" % user)
	latest = user
	emit('my message', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
	print("%s disconnected")
	print('Client disconnected')

@socketio.on('join')
def addClientToRoom(data):
	print(data)
	username = data['name']
	room = data['room']
	join_room(room)
	send(username + ' has entered the room.', room=room)

# braodcast to all connected sockets
def broadcast(data, room=None):
	print("broadcasting", data)
	if room:
		# use this for out of http context emiting of messages
		socketio.emit('my response', data, room=room)
	else:
		socketio.emit('my response', data, broadcast=True)
	pass

# sample function to demo/test sending to sid.
def sendToLatest(message):
	if latest:
		# use this for out of http context emiting of messages
		socketio.send(message, room=latest)

def webApp_Thread(debug=True, use_reloader=False):
	# socketio.run must be after all the event definations are declared
	#	if using flask run, this will not be important
	#	https://stackoverflow.com/questions/51525261/python-flask-socketio-working-not-receiving-data-from-js-client
	socketio.run(app, debug=debug, use_reloader=use_reloader)

def startServerThread():
	#disable reloader
	print("starting webApp in thread...")
	thread_webApp = threading.Thread(name="webApp", target=webApp_Thread)
	thread_webApp.daemon=True #
	thread_webApp.start()

if __name__ == '__main__':
	print("starting flask app")
	# call webApp_Thread() to start it normally
	webApp_Thread()
