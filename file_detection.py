# file detection

import os

path = "C:\\Users\\USER\\OneDrive - International Islamic University Malaysia\\Documents\\VS code\\file detection.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("It is a directory!")
else:
    print("That location not there!")