#The Code Revolution
#Lesson 8, Part II
#Importing functions in a module

#This exercise makes use of our pizza.py file
#we will import the functions from that file and use it here
#this sets us up to start learning about classes in the next exercise

#Save this file as Lesson 8.2.py or something :)
#and make sure it's stored in the same directory as your pizza.py file

import pizza

size = input("What size pizza would you like? S, M or L: ")
crust = input("What style of crust would you like: Thin, Regular or Deep Dish? ")
toppings = []
topping = ""
while topping != "quit":
    topping = input("Enter your toppings one line at a time, or 'quit': ")
    #add a line not to add the 'quit' as a topping
    toppings.append(topping)

#now call the makeapizza function in the pizza module
pizza.makeapizza(size, crust, toppings)


#we can also selecting import a function as follows:
from pizza import makeapizza
#and resusing the same variables above this should work:
makeapizza(size, crust, toppings)


#and we can further clarify our function to import
#by adding an alias
from pizza import makeapizza mp
mp(size, crust, toppings)

#last we can import every function in the modules as below
#this just allows us to skip the dot (.) notation when calling the function
from pizza import *
makeapizza(size, crust, toppings)
