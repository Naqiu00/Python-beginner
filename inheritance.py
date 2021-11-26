# inheritance

class animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(animal):
    def run(self):
        print("This rabbit is running")

class Fish(animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(animal):
    def fly(self):
        print("This hawkn is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
