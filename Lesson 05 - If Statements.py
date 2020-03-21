#The Code Revolution
#Lesson 05 - IF Statements
#Today we will tackle IF statements.  This is fundamental to programming
#and introduces control and logic to our programs
#That is, we can start to process data externally and ask
#questions and then make decisions about what to do next in the program
#If statements should start to become second nature to you.  Also in
#this lesson, as a 'bonus' we will start using functions to reall
#control the program flow and how we learn and interact with our
#program.  Functions don't really come into the curriculum until Lesson 08
#so if this feels a little advanced please be patient.
#Again, practice is the most important thing.
import time

"""
Using IF statements we use comparison operators
These are generally
== (equal to)
>= (greater than or equal to)
<= (less than or equal to)
>  (greater than)
<  (less than)
!= (not equal to)


Remember == (comparison) is different than = (assigment).
When we use = we are assigning the value on the right hand
side to the variable on the left hand side.  E.g.
myvariable = "Paul has a new ride"
"""
##############################
### OUR FIRST IF STATEMENT ###
##############################
def simpleIFexercise():
    #create a simple cars list
    cars = ["bmw", "jaguar", "subaru", "toyota"]

    #step through the list and compare the values
    for car in cars:
        if car == "bmw":
            print("We found a German Car: " + car.upper())
        else:
            print("Not a BMW at least: " + car.upper())

##############################
######## IF WITH CASE  #######
##############################
def ifwithcase():
    #now let's adapt the example for case
    cars = ["bmw", "jaguar", "subaru", "toyota"]
    for car in cars:
        if car.upper() == "BMW":
            print("We found a BMW: " + car.upper())
        else:
            print("Not a BMW or bmw: " + car.upper())
            
##############################
#####   IF WITH NUMBERS ######
##############################
def ifwithnumbers():
    #evaluating for multiple examples:
    #create a list of 'ages'
    ages = [22, 18, 75, 34, 40, 9]
    for age in ages:
        if (age > 21 and age < 35):
            print("We found the right age: " + str(age))
        else:
            print("The age found outside our defined range: " + str(age))

    #same as above but changing to -or-
    for age in ages:
        if (age > 21 or age < 35):
            print("We found the right age: " + str(age))
        else:
            print("The age found outside our defined range: " + str(age))


##############################
#####   IF WITH SEARCH  ######
##############################
def ifwithsearches():
    #create a list of names and then ask for a user input
    names = ["james", "paul", "scott", "anna", "deb"]
    search_string = input("Search for a name in the list: ")
    type(search_string)
    if search_string in names:
        print("Congratulations, you win!  We found your " + search_string)

##############################
#####  IF WITH BOOLEANS ######
##############################
def ifwithbooleans():
    #a simple boolean
    apples = input("Do you like apples? Type Yes or No: ")
    type(apples)
    likes_apples = False

    if apples == "Yes":
        likes_apples = True
    else:
        likes_apples = False

    if likes_apples:
        print("You like apples!")
    else:
        print("I can't believe you don't like apples!")

##############################
#####   USING ELIF      ######
##############################
def usingelif():
    #Using ELIF and ages
    input_age = input("What is your age? ")
    type(input_age)
    age = int(input_age)

    if age < 4:
        print("Your admission is free.")
    elif age < 18:
        print("Your admission is $7.")
    elif age < 55:
        print("Your admission is $10.")
    else:
        print("Your admission is $6.")
    
##############################
####  MAKE A PIE WITH IF #####
##############################    
def makingpizza():
    #making a pizza take some time
    import time #we have to import the time library so that we can make Python "sleep" for each step

    pizza_steps = ["make dough", "add sauce", "add cheese", "add other toppings", "bake"]

    print("We're about to make a pizza. Note that some steps take longer than others!")
    for step in pizza_steps:
        if step == "make dough":
            print(step)
            time.sleep(5)
        elif step == "bake":
            print(step)
            time.sleep(10)
        else:
            print(step)
            time.sleep(1)

    print("We're done with your pie!")

    #making a pizza take some time
    import time #we have to import the time library so that we can make Python "sleep" for each step

    pizza_steps = []

    #just make sure that the pizza_steps list has values and then walk through the code
    if pizza_steps:  #this is basically saying "if pizza_steps is null or empty"
        print("We're about to make a pizza. Note that some steps take longer than others!")
        for step in pizza_steps:
            if step == "make dough":
                print(step)
                time.sleep(5)
            elif step == "bake":
                print(step)
                time.sleep(10)
            else:
                print(step)
                time.sleep(1)
        print("We're done with your pie!")
    else:
        print("Your pie has no steps!")











################################
#### MAIN PROGRAM CONTROL ######
################################
"""
This is a multi-line comment.  Multi-line comments are just that, multi-line
but they are beneficial because you don't have to prefix each line with a comment
character.

This is also the Python's entry point and we will be using this format from now on.
This lesson introduces functions as an example:
def functionname():
    print("this is a function.")
    
"""
print("Welcome to the Code Revolution's Lesson 05, IF Statements!")
time.sleep(1)
print("Today we will also introduce functions as a way to leverage IF statements")
time.sleep(1)
print("as well as improve the experience of the applicaiton.  Yes, this is an application!")
time.sleep(1)

print("Please make a choice below:")
print("1. Simple If example. \n2. If example with case. \n3. If with numbers")
print("4. Simple If 'Searching' \n5. If example with booleans. \n6. Using elif. \n7. Making a Pizza Pie.")

userchoice = int(input("=>"))
if userchoice == 1:
    simpleIFexercise()
elif userchoice == 2:
    ifwithcase()
elif userchoice == 3:
    ifwithnumbers()
elif userchoice == 4:
    ifwithsearches()
elif userchoice == 5:
    ifwithbooleans()
elif userchoice == 6:
    usingelif()
elif userchoice == 7:
    makingpizza()
else:
    print("Invalid selection. Re-run the program.")