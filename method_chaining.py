# method chaining = calling multiple method sequentially
#                   each call performs an action on the same object and return self

class car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

Car = car()

# Car.turn_on().drive()
# Car.brake().turn_off()
Car.turn_on()\
    .drive()\
        .brake()\
            .turn_off()