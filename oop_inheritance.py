# INHERITANCE
# HAVE MAIN CLASS & SUB CLASS
# SUB CLASS CAN USE ELEMENT (PROPERTIES & METHOD) FROM MAIN CLASS
# PUBLIC CLASS EXAMPLE

class Human(object): # MAIN CLASS
    name = None

    def __init__(self, name): # function of properties
        self.name = name

    def play(self):
        print("{} play mobile game".format(self.name)) # function of method

class Human_Now(Human): # SUB CLASS
    email = None

    def set_email(self, email):
        self.email = email

    def info(self):
        print("name ={}, email ={}".format(self.name, self.email))

programmer = Human_Now("rangga")
programmer.set_email("rangga@google.com")
programmer.info()

farmer = Human_Now("izam")
farmer.set_email("izam@google.com")
farmer.info()

doctor = Human_Now("ifa")
doctor.set_email("ifa@google.com")
doctor.info()
