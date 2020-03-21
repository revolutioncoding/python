#The Code Revolution
#Lesson 09
#Classes (and OOD / OOP)

##################
#### Car Class ###
##################
import datetime #to calculate car age

class Car():
    """ A new car class and this is a multiline
        comment in Python """
    """
        the __init__ method is a standard initialization method in Python
        it has two leading and two trailing underscores
        the self parameter is required and it mmust come first
        but we won't need to provide this argument when we call this method
    """
    def __init__(self, make, model, year, mileage = 0):
        """ Initialize make and model attributes
            Any variable prefixed with self makes that variable available
            to any method in the class
        """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    #note this method only takes the 'self' argument
    def accelerate(self):
        """Will make the car go"""
        print(self.make.title() + " " + self.model.title() + " is speeding up!")

    #also this method only takes the self argument
    def brake(self):
        """Will make the car slow"""
        print(self.make.title() + " " + self.model.title() + " is slowing down.")

    def age(self):
        today = datetime.datetime.now()
        print("Your car is " + str(today.year - self.year) + " years old.")

    def updatemileage(self, mileage):
        self.mileage = mileage
        print("Your car's odometer has been updated to: " + str(mileage))

