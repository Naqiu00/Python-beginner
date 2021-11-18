#nested func calls = function calls inside other function calls, innermost function resolved first

# num = input("Enter a whole number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a POSITIVE number: ")))))