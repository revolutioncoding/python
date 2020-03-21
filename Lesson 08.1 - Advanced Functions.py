#Lesson 08
#The Code Revolution
#Advanced Functions

#We've actually jumped into functions a little early in the last few
#lessons to make running and testing our code cleaner and easier to use
#In this lesson we will dig further into functions and how they
#can be used to do additional things like:
# 1. Passing arguments / parameters
# 2. Using return values
# 3. Optional Arguments
# 4. Returning more complex types like Dictionaries & Lists
# 5. Using arbitrary arguments
# 6. Storing functions in modules
# 7. Importing modules and functions

##############################
### ARGUMENTS & PARAMETERS ###
##############################

def usingarguments(randomnumber):
    #we will demonstrate
    print("The argument passed to this function is: " + str(randomnumber))
    #the 'randomnumber' is called the parameter
    #the 'userchoice' VALUE passed is the argument

def usingpositionalarguments(string1, string2):
    #when we use positional arguments, that means the position
    #of the argument in the function call will associate to the
    #parameter in the function
    print("The first argument is: " + string1)
    print("The second argument is: " + string2)

#when we use keyword arguments we provide the parametername='value' in
#the function call.  that way we don't have to be concerned about the order
#that the arguments are provided
def usingkeywordarguments(string1, string2):
    print("This should demonstrate keyword arguments:")
    print("We don't have to specify the order if we associate the arguments")
    print("to the parameter names.")
    print("The first parameter string1's argument value is: " + string1)
    print("The second parameter string2's argument value is: " + string2)

#The 2nd parameter below is optional because we are supplying
#a default value when a value is not passed
def usingdefaultvalues(string1, string2="string2"):
    print("Using Default values we can set a parameter value by default")
    print("In this case our 2nd parameter has a value of 'string2'")
    print("String1 value: " + string1)
    print("String2 value: " + string2)



##################################
###   USING RETURN VALUES   ######
##################################

#To make things easier we can provide a return value to the calling function
#so that we can allow the calling function to process the data
#we've already done this with the input function
#i.e. input("Some question for the user") returns a string that we
#do something with.  If we do nothing with that value, nothing happens
#Using return values is the same because we just return the data to the caller
#function and decide what to do with the data at that point

def returningavalue(firstname, lastname):
    #we will concatenate these arguments and title() them
    #then return the formmated string
    fullname = firstname.title() + " " + lastname.title()
    return fullname



##################################
###   OPTIONAL ARGUMENTS    ######
##################################

#Optional arguments are the same as default values in arguments.
#The difference is that we set the default value to be an empty
#zero length string.  I.e. optionalvalue = ""

def usingoptionalvalues(optional=""):
    if len(optional) == 0:
        print("You did not provide any optional value to the function.")
    else:
        print("The value you provided was: " + optional)

##################################
### RETURNING COMPLEX VALUES #####
##################################

#in this example we will return a dictionary to the calling function
def createaperson(firstname, lastname, age):
    person = { "first": firstname,
               "last": lastname,
               "age": age}
    return person

##################################
###   ARBITRARY ARGUMENTS    #####
##################################

#Python allows us to pass an arbitrary number of arguments
#assuming the data passed can change from call to call, we want to be flexible
def makemeapizza(*toppings):
    for topping in toppings:
        print("Topping: " + topping)

##################################
### MAIN USER INPUT SECTION ######
##################################
print("Welcome to the Code Revolution Lesson 8 - Functions!")
print("Please choose a mini exercise to test!")
print("1. Passing arguments and parameters\n2. Using return values")
print("3. Optional Arguments\n4. Returning complex values")
print("5. Using arbitrary arguments")
userchoice = input("=>")

#let's introduce a new concept, called the try to try "something"
#first so we can control what happens if there's an error
try:
    userchoice = int(userchoice)
except:
    print("You did not enter a correct number choice. Please restart.")

if userchoice == 1:
    usingarguments(userchoice)
    usingpositionalarguments("first", "second")
    usingkeywordarguments(string2="this is string2", string1="this is string1")
    # note this function has two parameters but we are only
    # passing one argumet
    usingdefaultvalues("just one argument")
    passdatatodefault = input("Enter some text to pass to the default value: ")
    # but in this case we are passing two arguments to the same function
    usingdefaultvalues("just one argument", passdatatodefault)
elif userchoice == 2:
    fname = input("What is your first name? ")
    lname = input("What is your last name? ")
    #I changed the variable names here not to match the parameter names
    #just to reitirate that it's the order that's important
    #otherwise we have to use the keyword arguments above
    fullname = returningavalue(fname, lname)
    print("Your formatted name is: " + fullname)
elif userchoice == 3:
    #calling a function with an optional value passed
    usingoptionalvalues("Here's an Optional Value")
    #calling the same function without a value passed
    usingoptionalvalues()
elif userchoice == 4:
    fname = input("What is your first name?")
    lname = input("What is your last name?")
    age = int(input("How old are you in years?"))
    
    person = createaperson(fname, lname, age)
    print("The person you created is:")
    for key, value in person.items():
        print(key, ": ", str(value))

elif userchoice == 5:
    print("Review in your own time Using Arbitrary Arguments in Python.")
    print("My preference here would be to use a List.")
    makemeapizza("pepperoni", "cheese", "mushrooms")
    makemeapizza("cheese")
    
