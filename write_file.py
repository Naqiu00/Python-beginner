# write a file

text = "Goodluck learning"

with open('test.txt', 'a') as file:
    file.write(text)

with open('test.txt', 'w') as file:
    file.write(text)