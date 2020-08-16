import socketio
import asyncio

# standard Python
sio = socketio.Client()

@sio.event
def message(data):
	print('I received a message!', data)

@sio.on('my response')
def on_message(data):
	print('I received a MY RESPONSE message!', data)
	return "OK", 123 #optional return

@sio.event
def connect():
	print("Connected! Joining room")
	sio.emit("join", {'name':"Unique Client Name", 'room':"General"})

@sio.event
def connect_error():
	print("The connection failed!")

@sio.event
def disconnect():
	print("I'm disconnected!")

def main():
	sio.connect('http://localhost:5000')
	pass

if __name__ == '__main__':
	main()
