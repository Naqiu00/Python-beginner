# daemon thread = a thread runs in background, not important for program to run
                # program will not wait for the daemon thread to complete before exiting
                # non-daemon thread cannot be normally killed, stay alive until task is complete
                # ex. background task, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon)

answer = input("Do you wish to exit? ")
