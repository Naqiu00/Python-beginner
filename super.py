# super = func used to give access to the methods of a parent class. returns a temporary object of a parent class when used

class rect():
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width
    
class square(rect):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)
    
    def area(self):
        return self.length*self.width

class cube(rect):
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

Square = square(3, 3)
Cube = cube(3, 3, 3)

print(Square.area())
print(Cube.volume())