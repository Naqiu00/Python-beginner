# class variable

from car_class import car

car_1 = car('Proton', 'X50', 2021, 'red')
car_2 = car('Perodua', 'Myvi', 2022, 'silver')

car_1.wheels = 2
# car.wheels = 2

print(car_2.wheels)
print(car_1.wheels)