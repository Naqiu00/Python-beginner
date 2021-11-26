class car:

    wheels = 4      # class variable

# special method called __init__(self) = construct object
# also called constuctor
    def __init__(self, make, model, year, colour):     
        self.make = make        # instance variable
        self.model = model      # instance variable
        self.year = year        # instance variable
        self.colour = colour    # instance variable

    def drive(self):
        print("This {} is driving.".format(self.model))

    def stop(self):
        print("This {} is stopped.".format(self.model))

    