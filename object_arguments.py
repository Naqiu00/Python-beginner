# pass object as arguments

class Car:

    colour = None

class Motorcycle:

    colour = None

def change_colour(car, colour):

    car.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_colour(car_1, "red")
change_colour(car_2, "blue")
change_colour(car_3, "white")
change_colour(bike_1, "green")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(bike_1.colour)