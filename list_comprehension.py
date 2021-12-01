# list comprehension = a way to create new list with less syntax
#                      mimic certain lambda function, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression (if/else) for item in iterable]

# square = []                 # create empty list
# for i in range(1,11):       # create for loop
#     square.append(i * i)    # define what each loop iteration should do
# print(square)

# squares = [i * i for i in range(1,11)]
# print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# passed_student = list(filter(lambda x:x >= 60, students))
# passed_student = [i for i in students if i >= 60]
passed_student = [i if i >= 60 else "Failed" for i in students]

print(passed_student)