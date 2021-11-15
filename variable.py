#variable = container to store a value. The value assign can be in different data type not limited to number or int

# string
first_name = "Chris"
last_name = "Patt"
full_name = first_name + " " + last_name
#you can get the data type of the variable by printing type
print(type(first_name))
print(first_name)
print(last_name)
print("My name is " + full_name)

#int 
age = 24
print(type(age))
print(age)
age += 1
print(age)

print("My name is " + full_name + ", and I am " + str(age) + " years old.")

#float
height = 179.9
weight = 68.5
print(height, weight)
print("My height and weight are " + str(height) + ", " + str(weight))

#boolean
sick = True
print("Are you sick : " + str(sick))