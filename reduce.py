# reduce() = apply function to iterable and reduce it to single cumulative value, perform function on first two elements and repeat until 1 value reamains

# reduce(function, iterable)

import functools

# letters = ["H", "E", "L", "L", "O"]
# word = functools.reduce(lambda x, y: x + y, letters)
# print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x * y, factorial)
print(result)