# abstract classes
    # prevent user from creating an object of that class 
    # user need to override abstract methods in child class

# abstract class = class contains one or more abstract methods
# abstract method = method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stopped the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")
    
    def stop(self):
        print("You stopped the motorcycle")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()