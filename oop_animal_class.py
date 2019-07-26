# Classes are the basis of OOP - Object Orientated Programming
#**They are cookie cutters for objects**.
#From classes you initialise individual instances of this class
# Classes hold methods (methods are functions that depend on instances of classes. They can only be called on instances of a class

class Animal():

    def __init__(self): # Constructor method runs whenever an instance is
        # Self parts are properties of the animal
        self.name = 'Ringo'
        self.species = 'Lizard'
        self.age = 7
        self.alive = True

    #Methods for Class Objects - Instances
    def sleep(self): # Self refers to the instance if it gets called upon - self populates the self with the instance
        return 'zzzz'

    def eat(self, food):
        return 'nom NOM nom NOM this was some good ' + food

    def potty(self):
        return "... .... uuhh 0.o --- SLPOGH! 0.0 ... -.-"


# #Since there is no connection to the database, the instances are not stored and are automatically removed
# animal_1 = Animal() # Creating one instance of class Animal
# # print(animal_1)
# # print(type(animal_1))
#
# # Calling methods on instances of animal
# print(animal_1.sleep())
# print(animal_1.eat('meat salad'))
# print(animal_1.potty())
#
# # Accessing properties of instance of animal
# print(animal_1.name, animal_1.age) #Having several arguments on one line is known as overloading
# print(animal_1.age)

