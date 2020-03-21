#The Code Revolution
#Lesson -  07 User Input and While Loops
#We've been using User Input for a while now, as it's a nice way
#to control the program flow.  This lesson formally introduces them and
#just addresses some of the formalities around their use that we may
#have not covered previously

import time

#Like all exercises at the Code Revolution we will actually use the USER INPUT to control
#the program flow.  This is like a 'Console Application' that allows the user
#to make choices


#################################
#######  USER INPUT TIPS ########
#################################
def userinputtips():
    #use a variable to accept the user input and then assign it to that input
    #be aware of how the text prints on the screen and add things like extra
    #spacing at the end of a input statement to the user doesn't start typing
    #immediately against the input prompt.
    example = input("Enter some text to store in the 'example' variable: ")
    print("The data stored in example is: " + example)
    
    #You can also use the \n (new line character) to insert a new line inside any text
    name = input("Enter your name: ")
    print("\n\nHello, " + name + "! And Welcome to the Code Revolution!!!")
    
    
def userINTinput():
    #this example just demonstrates how to convert the string input
    #to an int if that is the data you are after
    #just like we've used the str() function to convert an int to a string
    #we can use the int() function to convert a string to an int
    age = input("How old are you ?")
    age = int(age) #this also emphasizes the 'dynamic' nature of python
    print("Evaluating if you are older than 18...")
    time.sleep(2)  #make the computer "think" for 2 seconds
    print(age > 18)
    time.sleep(2)
    if(age > 18):
        yearssince18 = age - 18
        print(str(yearssince18) + " you turned 18!")
    else:
        yearsto18 = 18 - age
        print("You will be 18 in :" + str(yearsto18) + " years")
        
        
#################################
########    MODULO  #############
#################################
#The Modulo operator is the remainder after a division operation
#it is useful when you are working in a list or dataset and want to know
#if you are on an even row count, odd row count or even, every 3rd row
#In a simple sense when you think about a grid of data on a web page
#the modulo operator would allow us to know, with certainty, the even rows
#so we could provide some different formatting
def modulotests():
    number = input("Enter a number and we will check if it's evenly divible by two: ")
    number = int(number)

    if number % 2 == 0:
        print(str(number) + " is an even number.")
    else:
        print(str(number) + " is an odd number.")
    

#################################
####### WHILE LOOPS   ###########
#################################
#A while loop will loop until some condition specified is met
#An example is probably more useful:
def basicwhileloop():
    loopcount = 1
    while loopcount <= 5: #less than or equal
        print("Current Loop count: " + str(loopcount))
        time.sleep(1) # just to see the loop "in action"
        loopcount += 1 #increment the loop count otherwise this loop will be infinite
    
    
    #This loop will demonstrate a deliberate infinite while loop
    #but provides the user an option to quit.  I.e. our while condition is the quit condition
    message = ""
    while message != "quit":
        message = input("Enter some characters and the computer will tell you the length!  Enter quit to quit.")
        print(len(message))
 
 
#################################
### WHILE LOOPS WITH BOOLEAN ####
#################################
#We are going to use a flag (aka boolean True/False value) to break the loop
def whileloopwithflag():
    message = ""
    active = True
    while active:
        message = input("Enter some characters and the computer will tell you the length!  Enter quit to quit.")
        
        if message == "quit":
            active = False
        else:
            print(len(message))
            
#################################
### WHILE LOOPS WITH BOOLEAN ####
#################################
#We are going to skip using the boolean flag and and just use a break to exit the loop
def whileloopwithbreak():
    message = ""
    while True:
        message = input("Enter some characters and the computer will tell you the length!  Enter quit to quit.")
        
        if message == "quit":
            break  #this will exit the loop at this point so any code below will not be executed
        else:
            print(len(message))
            

#################################
### WHILE LOOPS WITH BOOLEAN ####
#################################
#The continue keyword allows us to restart the loop again and bypass any code below.  But keeps the loop running
def whileloopwithcontinue():
    loopcount = 0 
    while loopcount <= 10:
        loopcount += 1
        if loopcount % 2 == 0:
            continue
        print("Only odd values should be printed: " + str(loopcount))
        time.sleep(1)
        
##################################
###### LOOPS WITH LISTS   ########
##################################
#for this exercise we will move list items from one list to another
#the loop condition will be to run until the first list is empty
def whileloopwithlists():
    newstudents = ["john", "peter", "paul"]
    processedstudents = []
    while newstudents:  #this is basically saying that whie the list exists and contains items
        currentstudent = newstudents.pop()
        print("Processing: " + currentstudent)
        time.sleep(1)
        processedstudents.append(currentstudent)
        
 
 
##################################
#### LOOPS WITH DICTIONARIES #####
##################################
#in this example we will take some user input and store
#these values in a dictionary
def whileloopswithdictionaries():
    heights = {}
    polling = True
    while polling == True:
        #ask for a person's name and height
        #and then ask the poll worker if there are more
        #people to survey
        name = input("What is the person's first name?")
        height = input("What is the person's height in inches?")
        height = int(height)
    
        heights[name] = height
    
        repeat = input("Are there more people to survey? Enter yes or no.")
        if repeat == "no":
            print("Polling complete, compiling results...")
            polling = False
    
    #print the poll results
    for name, height in heights.items():
        print(name + " is " + str(height) + " inches tall.")
        
        
#################################
###### PROGRAM START  ###########
#################################
        
print("Welcome to our intro to Input and Loops!!!")
print("Make your choice below and make it wisely!")
programinput = "1. Test basic user input.\n2. Test user input with integers\n"
programinput += "3. Use the modulo operator.\n4: Basic While Loops\n5: While Loops with a Flag or Boolean\n"
programinput += "6: While Loops with a 'break'\n7: While Loops with a 'continue'\n"
programinput += "8: While Loops with Lists\n9: While Loops with Dictionaries\n=>"
choice = input(programinput)


choice = int(choice)
if choice == 1:
    userinputtips()
elif choice == 2:
    userINTinput()
elif choice == 3:
    modulotests()
elif choice == 4:
    basicwhileloop()
elif choice == 5:
    whileloopwithflag()
elif choice == 6:
    whileloopwithbreak()
elif choice == 7:
    whileloopwithcontinue()
elif choice == 8:
    whileloopwithlists()
elif choice == 9:
    whileloopswithdictionaries()
else:
    print("No valid choice selected.  Rerun your python file to start over.")