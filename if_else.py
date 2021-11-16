#if statement = block of code that executed when the condition is true

age = int(input("How old are you : "))

if age == 100:
    print("You are very old!!")
elif age >= 18:
    print("You are an adult")
elif age <0:
    print("You havent been born yet!!")
# use == for equal instead of =
else:
    print("You are a kid")
