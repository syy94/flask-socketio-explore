# flask-socketio Exploration
This repository explores a way to start a flask_socketio web App on a new thread and how to use the socketio APIs.

### Server(Threaded) (main.py)
The server periodically broadcast to all sockets connected to it. The server will also send a message to the latest connected socket periodically.
### Server(Threaded) (server.py)
Responds to client connection/disconnection only.
### Client (client.py)
The server is tested with a client script using python-socketio[client].
You can have multiple consoles/terminals running to simulate multiple clients.

# Setup
## Libraries
Run **pip install -r requirements.txt** to install all the libraries used.
## Usage
Execute **python main.py** to start the server in a background thread.

Execute **python server.py** to start the server normally.

# Issues
This exploration is done locally only. These scripts have not been deployed and tested.

# Links
- [flask-socketio](https://flask-socketio.readthedocs.io/en/latest/)
- [python-socketio](https://python-socketio.readthedocs.io/en/latest/index.html)
