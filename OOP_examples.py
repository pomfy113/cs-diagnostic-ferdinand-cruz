import sys, os

# Initializes car; takes in a color
# Moved the methods to the automobile from car
class Automobile(object):
    def __init__(self, color):
        self.color = color
        self.model = "Toyota"

    # It beeps!
    def honk(self):
        print "Beep beep!"

    # prints out the attributes and their number
    def description(self):
        print vars(self)

# Motorcycles have two wheels and that's all I've got man
class Motorcycle(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.wheelNum = 2
        self.make = "Ducati?"
        self.topSpeed = 70

# 4 wheels this time! I don't know about cars either
class Car(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.wheelNum = 4
        self.make = "Accord?"
        self.topSpeed = 100

# These are the ones with a lot of wheels right?
class SemiTruck(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.wheelNum = 16
        self.make = "Big Rig?"
        self.topSpeed = 60

#test stuff
if __name__ == "__main__":
    test1 = Car("Red")
    print test1.color
    print test1.topSpeed
    test1.honk()
    test1.description()

    test2 = Motorcycle("Green")
    print test2.color
    print test2.topSpeed
    test2.honk()
    test2.description()
