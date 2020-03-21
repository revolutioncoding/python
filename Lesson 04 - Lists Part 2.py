#The Code Revolution
#Lesson 04
#Lists II

# In this lesson we are going to build familiarity with Lists.
# This should be a relatively short exercise in Lists and overlap with our last lesson
# We will be using a new concept, a loop, specifically a 'for loop' to iterate through lists
# for loops are very common ways to work with the data (i.e. values) in lists
# We'll also be using the time.sleep function to make interactions with lists more interesting
# Here at the Code Revolution we like to introduce new concepts outside the standard lesson
# to make the experience more interesting as well as to teach something new
# Today's bonus we'll be using the time library to slow down our output
# in order to use the time library (or any library in python) we must tell python
# we will be using it in our code.  to do this, we add an 'import library' statement:
import time


####################################
#### USING FOR LOOPS WITH LISTS ####
####################################


#create a simple list
students = ['paul', 'peter', 'mary']
for student in students:
    print(student.title() + " is a student at the Code Revolution!")
    #put the loop to sleep for one second to make the output slightly more interesting...
    time.sleep(1)
    
#note above too how the time.sleep(1) function is part of the loop because it is indented
#in Python indentation (i.e. formatting) is part of the structure of a loop
#other languages use curly braces ,i.e. {}, to wrap a loop.
#so we need to be aware of common mistakes when forgetting our indentation rules:
    
#accidental indentation
message = "The Revolution is coming"
    print(message)
#this will throw an error in the shell output: 'unexpected indent'
#this also introduces another common coding practice.  sometimes its easier to
#comment a line rather than delete it.  we may need the code later as a reference
#in the case above we will just comment the line out to continue the lesson and leave it
#there as an example

#forgetting the colon on a loop
for student in students
    print(student) #this will just generate an 'invalid syntax' error

###################################
#### USING THE RANGE FUNCTION #####
###################################
    
#the range function is a special python function that allows
#us to quickly generate a numeric list or use it in a loop
print("We are going to create a loop from a range(1, 5)")
print("and then sleep for that number of seconds each iteration")
for value in range(1, 5):
    print("The loop variables is: " + str(value))
    time.sleep(value)

#similarly we can use the range function to create a list
somenumbers = list(range(1, 6))
#note how we use the 'list' before the range function to convert the numeric range to a list
#this is similar to how we've used the str() function to convert a number to a string
#just to illustarte what this looks like, let's print it
print("We converted a range(1, 6) to a list and then we'll print it below")
time.sleep(2)
print(somenumbers)

#let's create a list of even numbers
evennumbers = list(range(2, 11, 2)) #using a 'step' value of 2
print("Only printing our even numbers list")
time.sleep(2)
for evennumber in evennumbers:
    print(evennumber)
    time.sleep(1)
#remember evennumber is a loop variable that is declared / initialized
#as part of the for loop.

#let's create an empty list and assign it the result of squaring some numbers
squares = []
for value in range(1, 11):
    square = value**2 #the ** indicates an exponent, 'to the power of'
    squares.append(square)
    print("The square of " + str(value) + " is " + str(square))
    time.sleep(1)
    
##################################
##### SLICING A LIST #############
##################################

#we can use the list[index: index] to specify a portion of that list
#for example if we have the following list
newstudents = ["paul", "john", "edward", "jen", "sarah", "chrissy"]
#the first three students would be:
firstthree = newstudents[:3]
print("the first 3 students (i.e. newstudents[:3]) in our list are:")
time.sleep(2)
for student in firstthree:
    print(student.title())
    time.sleep(1)
    
#there's also a way to get the last part of a list by using a negative
#this is useful when you're not sure how many values are in the list
lastthree = newstudents[-3:]
print("printing the last three via newstudents[-3:]")
time.sleep(1)
for student in lastthree:
    print(student.title())
    time.sleep(1)
    
##################################
##### COPYING A LIST #############
##################################

#the first students of the code revolution are:
originalstudents = ["ryan", "logan", "noah", "michael", "tyler"]
#now create a new list below and assign its value from the originalstudents
currentstudents = originalstudents
currentstudents.append("your name")
#now let's see what happens when we print our originalstudents list
print("Printing the list of originalstudents after we copied it to a new list and updated that list")
for student in originalstudents:
    print(student.title())
    time.sleep(1)

#Note that when you appended a student to currentstudents list it update
#the original students list as well.  This is how Python works
#we've actually just created a list that references the first
#so it's deceptive because we don't really have two lists
#here are three ways to work around this

#slicing to copy
students2 = originalstudents[:]
students2.append("new name") #choose a different name here

#test this by printing both lists
print("Original Students:")
print(originalstudents)
print("students2:")
print(students2)
time.sleep(1) #just to provide some separation in the output

#using the built in copy method
students3 = originalstudents.copy()
students3.append("third name") #again choosing a different name
print("Original Students:")
print(originalstudents)
print("students3:")
print(students3)
time.sleep(1)

#using the list conversion function to copy:
students4 = list(originalstudents)
students4.append("fourth name") #again choosing a different name
print("Original students:")
print(originalstudents)
print("students4:")
print(students4)

####################
##### TUPLES #######
####################

#Tuples are like lists except that once they are created, they canot
#be modified. This is useful when you want their values to be static
originalstudents = ("Ryan", "Logan", "Noah", "Michael", "Tyler")

#looping is similar
for student in originalstudents:
    print("Student in the tuple: " + student)
    time.sleep(1)
    
#try adding a student    
originalstudents.append("Paul")
#try renaming a student
originalstudents[0] = "Paul"
