# map() = apply a function to each item in an iterable(list, tuple, etc)

# map(function, iterable)

store = [
    ("Shirt", 20.00),
    ("Jacket", 25.00),
    ("Pant", 15.00),
    ("Socks", 9.00)
]

to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)

store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)