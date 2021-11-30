# lambda function = function written in 1 lineusing lambda keyword
#                   accept any number of arguments, but only has one expression
#                   a shortcut, usefulif needed for a short period of time

# lambda parameters:expression

# def double(x):
#     return x * 2

# print(double(5))

double = lambda x:x * 2
multiply = lambda x, y:x * y
add = lambda x, y, z:x + y + z
full_name = lambda first_name, last_name:first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
print(full_name("Chris", "Patt"))
print(age_check(18))