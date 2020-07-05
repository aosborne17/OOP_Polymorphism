class Bird:
    """
    Polymorphism allows us to define the same methods in our parent class
    to our child class but the change the outcome of the method
    This is helpful if the action of the parent class is not exactly what
    we want for the child class
    """
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

"""
As we can see, we have the same method 'flight', but in the subclass
it's action has been changed slightly to print something else.
"""

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")





class Animal:
    def __init__(self, colour, mood, hungry, sleepy):
        self.colour = colour
        self.mood = mood
        self.hungry = True
        self.sleepy = True

    def eat(self):
        self.hungry = False
        print("I am no longer Hungry :) ")

    def sleep(self):
        self.sleepy = False
        print("Got my beauty sleep!!")

    def procreate(self):
        print("ooh another Kid")

    def create_being(self):
        input("What would you like to call your being?: ")


"""
The subclass Mammal has inherited from the Animal parent class,
however it also has some additional attributes and methods.
Mammals can also be hairy and have the ability to lactate.
"""


class Mammal(Animal):
    def __init__(self, colour, mood, hungry, sleepy, hairy, lactate):
        super().__init__(colour, mood, hungry, sleepy)
        self.hairy = hairy
        self.lactate = lactate
    """
    We have added additional methods as well, 
    mammals can also hibernate and hunt.
    """
    def hibernate(self):
        self.mood = "Happy"

    def hunt(self):
        self.mood = "Tired"
        self.hungry = "Full"
