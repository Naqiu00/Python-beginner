# open a file

try:
    with open('C:\\Users\\USER\\OneDrive - International Islamic University Malaysia\\Documents\\VS code\\file detection.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
