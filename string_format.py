# str.format = for string, optional method that gives more control to display output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
# {} is the placeholder for value or variable
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))   # positional argument
print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon"))   # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

# add heading
name = "Chris"

print("Hello, my anme is {}".format(name))
print("Hello, my anme is {:10}. Nice to meet you".format(name))
print("Hello, my anme is {:<10}. Nice to meet you".format(name))
print("Hello, my anme is {:>10}. Nice to meet you".format(name))
print("Hello, my anme is {:^10}. Nice to meet you".format(name))

print("Hello, my anme is {name:^10}. Nice to meet you".format(name = "Bro"))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))
