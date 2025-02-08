# SAME CASE IN OOP PYTHON
class Human(object):
    name = None

    def __init__(self, name): # function of properties
        self.name = name

    def play(self):
        print("{} play mobile game".format(self.name)) # function of method

programmer = Human("rangga")
programmer.play()

farmer = Human("izam")
farmer.play()

doctor = Human("ifa")
doctor.play()

# __init__() is constructor (called by)