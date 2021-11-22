#scope = the region a variable is recognized. if the variable is declared inside a function, the variable cannot be recognize outside the function.
#a global and local variable can have the same name but it is consiodered different entity.

name_global = "Patt" #global variable (available inside and outside functions)

def display_name():
    name_local = "Chris" #name is a local variable( available only in this function)
    print(name_local)

# print(name) # calling name variable will give an error

print(name_global)
display_name()