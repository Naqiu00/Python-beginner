#type cast = convert a value of a data type to another data type

#int
x = 4
#float
y = 4.56
#string
z = "5" 

print(x)
print(int(y)) #not a permanent change
print(z)

#to make it permanent
y = int(y)
print(y)

print(z*3)
print(int(z)*3)
#to float
print(float(x))
#to string
print(str(x))

# print("X is " + x) #error
print("X is " + str(x))