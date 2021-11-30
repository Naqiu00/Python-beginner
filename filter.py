# filter() = create a collection of elements from an iterable for which a function returs true

# filter(funtion, iterable)

friends = [
    ("Chris", 20),
    ("Jack", 21),
    ("Susie", 16),
    ("Alya", 18)
]

age = lambda data:data[1] >= 18 

drinking_buddy = list(filter(age, friends))

for i in drinking_buddy:
    print(i)