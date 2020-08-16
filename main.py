import server
import threading
from datetime import datetime

# make sure in the flask server python code executes eventlet.monkey_patch
import asyncio #should be able to use other concurrency libs but only this and eventlet tested

# if server did not monkey_patch(), uncomment this
# import eventlet
# eventlet.monkey_patch()

async def BroadcastTask(message, room=None):
	server.broadcast(message, room)

async def RepeatedBroadcastTask(message, room=None):
	while True:
		await asyncio.sleep(2) # every 2 seconds
		await BroadcastTask("%s %s" % (message, getStrFormatTime()), room)

async def AnnoyLatestUserTask():
	while True:
		print("Annoy")
		await asyncio.sleep(5) #every 5 seconds
		server.sendToLatest("Hi Latest! %s " % getStrFormatTime())

def getStrFormatTime():
	return datetime.now().strftime("%H:%M:%S")

async def main():
	# Do stuff here

	# create_task to do things synchronously
	# broadcast to all
	repeatedTask = asyncio.create_task(RepeatedBroadcastTask("Repeated Message"))
	annoyTask =  asyncio.create_task(AnnoyLatestUserTask())

	while True: ## while loop to keep the server going
		await asyncio.sleep(1000) # handover for the other coroutines to execute
		pass

	# wait till i figure out a simple way to get user input from console
	#  so i can 'gracefully' stop the tasks and stop the server
	# repeatedTask.cancel()
	# annoyTask.cancel()

if __name__ == '__main__':
	server.startServerThread()
	asyncio.run(main())
