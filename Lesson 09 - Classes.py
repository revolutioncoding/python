#The Code Revolution
#Lesson 09
#Classes and OOD / OOP

"""
Step 1
Create the Car Class
"""
#Create a new Python file and save it as car.py
#Enter the code provided and save it in the same location as this file:


"""
Step 2
Object Instantiation
"""
#We will create an instance of the Car Class
#This is an important concept in OOD.  We create an Object: the Car.
#We call this: The Car Class
#From that object we create a new instance of the Car
#Its the "instances" of the class that we work with
#The Class is just the description of what the object can do

#Import the Car class
from car import Car
#call the __init__ method
mycar = Car("Mini", "Countryman", 2012)  #mycar is our new car instance!!!
#Then we can call the car methods
#METHODS are basically functions but for classes
#So when we say method we are implying that it's a function
#that is part of a class
mycar.accelerate()
mycar.brake()
#We can access the attributes within the car instances
print("My car's make is: " + mycar.make.title())
print("My car's modle is: " + mycar.model.title())
#Allow the class to calculate your car's age
mycar.age()

#We can continue creating multiple instances
yourcar = Car("Honda", "Civic", 2010)
yourcar.accelerate()
yourcar.brake()
print("Your car's make is " + yourcar.make.title())
print("Your car's model is " + yourcar.model.title())
#Allow the class to calculate and print your car's age
yourcar.age()


"""
Step 3
Modifying instance attributes
"""
#Now we can call our methods that actually update an attribute in the instance
mycar.updatemileage(59712)
print("Just to confirm my mileage via attribute: " + str(mycar.mileage))

"""
Step 4
Inheritance
"""
#Inheritance is when we create a class from another class and
#through that the child class will inherit attributes and methods
#from the parent class
#Create a new file called racecar.py and save it in the same location
from racecar import RaceCar
myracecar = RaceCar("Ford", "Mustang", 2012, "Dana Kilpatrick", 3)
myracecar.age()

"""
Step 5
Create a Driver object and use that as an argument and attribute of the
RaceCar class
"""
#first create the Driver
from driver import Driver
mydriver = Driver("Paul", "Daniel", "11/11/1975", 17)
paulscar = RaceCar("McLaren", "F1", 2018, mydriver, 5)
mydriver.ticker()
