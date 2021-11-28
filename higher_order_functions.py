# higher order functions = a function that either:
#                          1. accept function as an argument
#                          2. returns a function
# function treated as object in python

# -------- 1st example ---------

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Hello")
#     print(text)

# hello(loud)
# hello(quiet)

# -------- 2nd example ---------

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))