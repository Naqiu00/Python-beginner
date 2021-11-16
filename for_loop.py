import time
#for loop = a statement that will execute it's block of code fo a limited amount of times

for i in range(10):
    print(i + 1)

#range(start, stop); start is inclusive while stop is exclusive
for i in range(50, 100):
    print(i)

#3rd argument is step
for i in range(50, 100, 2):
    print(i)

for i in "Chris Patt":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
    print("hyeee!!")