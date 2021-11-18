#keyword arg = arguments preceded by an identifier when pass to a function.
#the order does not matter as the function will know the names of the arguments that were pass.

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last = "Patt", first = "Chris", middle = "James")