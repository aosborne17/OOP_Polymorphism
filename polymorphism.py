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
