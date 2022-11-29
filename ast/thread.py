# SuperFastPython.com
# example of running a function in another thread
from time import sleep
from threading import Thread
 
# a custom function that blocks for a moment
def task(name,sleep1):
    while True:
        # block for a moment
        sleep(sleep1)
        # display a message
        print(name)
 
# create a thread
thread = Thread(target=task, args=(["papa",5]))


# run the thread
thread.start()

print("here")

