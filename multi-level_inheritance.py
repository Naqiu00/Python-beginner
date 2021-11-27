# multi-level inheritance = when a child class inherits another child class

class Organism:

    alive = True

class animal(Organism):

    def eat(self):
        print("This animal is eating")

class dog(animal):
    
    def bark(self):
        print("This dog is barking")


Dog = dog()
print(Dog.alive)
Dog.eat()
Dog.bark()