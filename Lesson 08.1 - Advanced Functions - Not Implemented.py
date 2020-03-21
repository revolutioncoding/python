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
    raise NotImplementedError
elif userchoice == 2:
      raise NotImplementedError
elif userchoice == 3:
    raise NotImplementedError
elif userchoice == 4:
    raise NotImplementedError    
elif userchoice == 5:
    raise NotImplementedError
    
