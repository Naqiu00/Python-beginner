# exception = events detected during execution that interupt flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a numbe rto be divided by: "))

    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can divide by zero!!!")
except ValueError as e:
    print(e)
    print("Use number only!!")
except Exception as e:
    print(e)
    print("something went wrong :( ")
else:
    print(result)
finally:
    print("This will always execute!")