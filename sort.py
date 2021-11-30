# sort() method = used with lists
# sort() function = used with iterables

#lists
# students = ["Squid","Sponge","Sandy"]

# students.sort(reverse=True)

# for i in students:
#     print(i)

#tuples
# students = ("Squid","Sponge","Sandy")

# sorted_students = sorted(students, reverse=True)

# for i in sorted_students:
#     print(i)

# list of tuples
# students = [
#     ("Squid", "F", 60),
#     ("Crab", "B", 25),
#     ("Sandy", "A", 10),
#     ("Sponge", "C", 39)
# ]

# grade = lambda grades:grades[1]
# students.sort(key=grade)

# for i in students:
#     print(i)

# tuple of tuples
students = (
    ("Squid", "F", 60),
    ("Crab", "B", 25),
    ("Sandy", "A", 10),
    ("Sponge", "C", 39)
)

grade = lambda grades:grades[1]
# students.sort(key=grade)
sorted_students = sorted(students, key=grade)

for i in sorted_students:
    print(i)