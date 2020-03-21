#The Code Revolution
#Lesson 02 (01 being installation and configurations)
#Today we will introduce variables and how we use them in Python
#With variables we will also talk about 'types'.  In programming,
#types are how we describe difference kinds of data and really objects
#There are two basic types we will introduce today:
#1. Strings
#2. Numbers

#Before we start however we are going to do some basic print statements and
#understand how to "run" the code.  The python print commmand is very basic
#but also very useful.  It serves as a guide when we're developing and testing
#our code.

################################
#####  PRINT STATEMENTS  #######
################################

#print some text, any text:
print("Some text")
#which is the same as:
print('some text')

#you can run this by going to the Run > Run Module
#alternatively you can hit F5 on your keyboard

#In python we can use either single quotes or double quotes.  We always need
#to wrap strings in quotes.  This is true of most programming languages.

#Congratulations you've just started using your first type in Python: Strings!
#You also just used your first function (i.e. print())

#Let's do something similar but use numbers and an operator to add or multiply
print(4200 * 1900)

#if we wrap the numbers above in quotes python will treat it as a string now
print("4200 * 1900")
#run / F5 this code and review the output

################################
#####      VARIABLES     #######
################################

#In python we do not have to delcare the variable type.  All variables are
#created the same.  I.e. variablename = "value"
#Python is considered dynamically typed.  This means that Python, when you 'run'
#your code will determine if your variable is a string, number or some other type
newmessage = "this is a new message"
print(newmessage)

newnumber = 7
print(newnumber)

#the newmessage variable above is a string.  newnumber is a number (integer)
#Here are some relevant facts about
#variables in Python
#-1- Can only contain letters, numbers and underscores.
#-2- Cannot start with a number

################################
#####       STRINGS      #######
################################

#Strings can use either single or double quotes, and even both
#We can alternate these quotes together when our string value requires
#one of the other (i.e. with contractions or actual quotes

randommessage = "I don't like to eat cake."
anotherrandommessage = 'Jane said: "I like to eat cake"'
print(randommessage)
print(anotherrandommessage)

#Note in the 2nd example if we try to use a don't:
#this line will not run
#anotherrandommessage = 'Jane said: "I don't like to eat cake'
#you will have to correct this line or comment it out.

##################################
##### STRING MANIPULATION  #######
##################################

#it is incredibly useful to know how to concatenate strings
#it is also useful to know how to convert non-strings to strings
#such that you can concatenate
#there are also various ways to change a string, like proper case,
#upper case, lower case, etc
#this is important because when comparing strings, case matters!!!

#string.title()
name = "paul kaman"
print(name.title())

#because most programming languages consider differing cases of the same letter
#to be different then we often have to convert strings to all lower case
#or all upper case to ensure the comparison is accurate.
#for example in Python:
#                      paul kaman is not the same as Paul Kaman
#to do a proper compare we would:
name = "paul kaman"
newname = "Paul Kaman"
print("Original Name: " + name)
print("New Name: " +newname)
print(name == newname) #this is a conditional and should print False

#the above comparison '==' is a more advanced concept so if it is unfamiliar
#don't focus on it, just continue through the coursework

#to compare like values we can use the title function:
print("Using .title() to alter a string value and compare.")
print(name.title() == newname.title())
#we can also use lower and/or upper functions
print("Using .upper to alter a string value and compare.")
print(name.upper() == newname.upper())
print("Using .lower to alter a string value and compare.")
print(name.lower() == newname.lower())

##################################
########### NUMBERS  #############
##################################

#Numbers are different from strings in that we can add, subtract, multiple, etc.
#Both Strings and Numbers make use of the '+' operation.  However, the difference is:
#Strings: + means we are concatenanting more than one string
#Numbers: + means we are adding

#Number variable
result = 5*2
print(result)

##################################
##### STRING AND NUMBERS  ########
##################################

#Often we will want to print a number with a string. But Python isn't sure if
#you're mistaken.  So it will throw an error. The line below should error out.
#Uncomment it, if it is commented out.
age = 43
name = "paul kaman"
print(name + " is " + age) #also not the use of padding spaces

#You should have gotten an error like:
##################################################################
##      TypeError: can only concatenate str (not "int") to str  ##
##################################################################

#This brings us full circle in our "types" lesson.  Python sees the two variables
#as different types. And Python isn't sure if we want to add or concatenate
#as such it throws an error and wants us to be more explicit
#We can be more explicit by CONVERTING our number to a string, as below:
print(name + " is " + str(age))
