# *args = parameter that will pack all arguments into a tuple. Useful for the function to be more flexible thing varying amount of arguments.

# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# print(add(1,2,3)) #no longer can use this if the parameter is more than 2

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9))