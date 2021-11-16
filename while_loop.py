#while loop = as the condition is true, it will execute it's block of code. Until the condition is false

#infinite loop
# while 1 == 1:
#     print("helpp!!")

name = None

while not name:
    name = input("Enter your name: ")

print("Hello " + name)