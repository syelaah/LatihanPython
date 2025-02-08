class Human(object): # MAIN CLASS
    name = None
    def __init__(self, name): # Function of properties
        self.name = name
    def play(self):
        print("{} play mobile game".format(self.name)) # Function of method
class Human_Now(Human):
    email = None # To be public
    __password = None # To be private (ENCAPSULATION)
    def set_email(self, email): # Public
        self.email = email
    def set_password(self, password): # Public
        self.__password = password
    def __hide_password(self): # To be private (ENCAPSULATION)
        return self.__password.replace("e", "*")
    def info(self): # Public
        print("name ={}, email ={}, password ={}".format(self.name, self.email, self.__hide_password()))

programmer = Human_Now("rangga")
programmer.set_email("rangga@google.com")
programmer.set_password("VerySecret")
programmer.info()

# ENCAPSULATION 2
# PERMITING SOME DEFINITE ELEMENTS
# PRIVATE CLASS & FUNCTION EXAMPLE
# print(programmer.__password)
# #Testing: AttributeError: 'Human_Now' object has no attribute '__password'

