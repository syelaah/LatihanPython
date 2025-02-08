# ENCAPSULATION
# PERMITING SOME DEFINITE ELEMENTS
# PRIVATE CLASS EXAMPLE

class Human(object): # MAIN CLASS
    name = None

    def __init__(self, name): # Function of properties
        self.name = name

    def play(self):
        print("{} play mobile game".format(self.name)) # Function of method

class Human_Now(Human):
    email = None
    __password = None # To be private (ENCAPSULATION)

    def set_email(self, email):
        self.email = email

    def info(self):
        print("name ={}, email ={}, password ={}".format(self.name, self.email, self.__password))

    def set_password(self, password):
        self.__password = password

programmer = Human_Now("rangga")
programmer.set_email("rangga@google.com")
programmer.set_password("secret")
programmer.info()

# print(programmer.__password)
# #Testing: AttributeError: 'Human_Now' object has no attribute '__password'