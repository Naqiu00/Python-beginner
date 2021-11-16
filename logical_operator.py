#logical operator = use to check two or more conditional statement is true
#(and, or, not)

temp = int(input("What is the temperature? "))
if temp >= 0 and temp <= 30:
    print("The temperature is good!!")

elif temp < 0 or temp > 30:
    print("temparature is bad")

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad!!")
