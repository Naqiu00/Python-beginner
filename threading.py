# thread = flow of execution. Ceach thread can carry out separate order of instruction
                # Each thread takes turn running to achieve concurrency
                # GIL = (global interpreter lock)
                # allows only one thread to hold the control of the Python interpreter at any one time

# cpu bounds = program/task spends most of it's time waiting for internal events(CPU intensive)
#              use multiprocessing

# io bounds = program/task spends most of it's time waiting for external events(user input, web scraping)
#             use multithreading

import threading
import time

def eat():
    time.sleep(3)
    print("You eat breakfast")


def drink():
    time.sleep(4)
    print("You drink coffee")


def study():
    time.sleep(5)
    print("You finish study")

x = threading.Thread(target=eat, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

# eat()
# drink()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())