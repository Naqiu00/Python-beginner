#tuples = unchangeable and ordered. used to group related data together

student = ("Chris", 24, "male")

print(student.count("Chris"))
print(student.index(24))

for x in student:
    print(x)

if "Chris" in student:
    print("His here!!")
