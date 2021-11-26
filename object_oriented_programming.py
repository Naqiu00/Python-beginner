# object oriented programming

'''
representation of real life object, 
combination of attributes(what the object has) and methods(what the object can  do)
using class, can be write in your main programming file or a different file
'''

from car_class import car

car_1 = car('Proton', 'X50', 2021, 'red')
car_2 = car('Perodua', 'Myvi', 2022, 'silver')

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.colour)

car_1.drive()
car_2.stop()