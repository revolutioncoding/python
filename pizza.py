#The Code Revolution
#Lesson 8, Part II
#Storing Code in Modules

#Save this files as pizza.py
import time

def makeapizza(size, crust, toppings):
    print("We are going to make a pizza...")
    print("Your specified pizza size is: " + str(size))
    print("Your crust type is: " + crust)
    time.sleep(1)
    print("Now let's add our toppings.")
    #we'll add 1 second of bake time for every topping
    baketime = 0
    for topping in toppings:
        print("Adding: " + topping)
        time.sleep(1)
        baketime += 1 #recall this is shorthand to adding 1 to our variable each loop

    print("Baking the pizza for " + str(baketime) + " seconds.")
    time.sleep(baketime)
    print("Your pizza is done!")
