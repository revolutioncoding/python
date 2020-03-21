#The Code Revolution
#Lesson 03
#Introducing Lists

#Lists are a useful concept in programming because it enables us to
#add multiple values to a single variable.  These 'types' are often called
#arrays in other languages.

#A simple list example is as follows:
shoppinglist = ['apples', 'oranges', 'paper towels', 'napkins', 'hot dogs']

#not the formatting difference here, the list is exactly the same
#as far as Python is concerned, but is much easier to read
shoppinglist = ['apples',
                'oranges',
                'paper towels',
                'napkins',
                'hot dogs']

#Python emphasizes readability in code.  The above is a best practice
#sometimes formatting is important.  In this case Python understands that the list
#continues on multiple lines.


##################################
#### BASIC LIST CONVENTIONS ######
##################################

#Lists use the brackets to wrap the values. I.e.
mylist = ['item1', 'item2', 'item3', 'item4']

#You then access list items by referencing the index value of that list item
#The index value is the ZERO based order
#In programming we used zero base to mean a sequence starting with 0, i.e.
#using our list above:
print(mylist[0]) #will print 'item1'
print(mylist[1]) #will print 'item2'
print(mylist[2]) #will print 'item3'
print(mylist[3]) #will print 'item4'

#for shoppint list it would be similar:
print(shoppinglist[0])
print(shoppinglist[1])
print(shoppinglist[2])
print(shoppinglist[3])
#what will these prints statements print?

##################################
##### MODIFYING LIST ITEMS #######
##################################

#This is important because we can reset an entire list if done incorrectly.  I.e.
shoppinglist = []
#that just blanked out our shopping list items
#a more appropriate thing (usually) is modifying individual list items
#let's rebuild the list
shoppinglist = ['apples',
                'oranges',
                'paper towels',
                'napkins',
                'hot dogs']

#MODIFYING: to modify the first item we use its ZERO based index:
shoppinglist[0] = "peaches"
print("Updated shopping list")
print(shoppinglist)

#######################################
###########     #ADDING:    ###########
#######################################

#to add (i.e. append) items to the list we use the .append function
shoppinglist.append("ketchup")
print("Appended list:") #we don't need to keep printing this text but it helps separate all our readouts from other print statements
print(shoppinglist)

#######################################
## Inserting, Updating and Removing ###
#######################################


#######################################
###########    INSERTING:    ##########
#######################################

#to insert an item into the list, you use the insert function
#which requires two arguments:
# 1. An index value for the order, and
# 2. the value

#if we want to put a priority on 'soda' for example:
shoppinglist.insert(0, "soda")
print("Inserted list update:")
print(shoppinglist)

#######################################
#########       REMOVING:     #########
#######################################

#to remove an item we can use the del keyword
del shoppinglist[0] #will delete the first item in the list
del shoppinglist[0] #will also delete the first item, but since we just
#delted the first item this will delete the item that was the 2nd item

#NOTE: We have to be careful about deleting and updating using Index values
#because it can be easy to overwrite or remove the wrong value

#######################################

#POP: to get the last item added we can use the .pop() function of the list object
lastitem = shoppinglist.pop()
print("the last item we added ot the shopping list is: " + lastitem)
print() #this last print statement is just to add some line formatting
#but this also alters the original list so:
print("Here is the list now that we've modified it, i.e. popped it.")
print(shoppinglist)

#We can also provide the item index in the pop function. I.e.:
firstitem = shoppinglist.pop(0)
#but recall now that we've taken (i.e. popped) the first item
#what is the value of the shoppinglist[0]?
#eventually this will error.
#enter the lines below and remove the comment prefix (#) and run the program
#seconditem = shoppinglist.pop(1)
#thirditem = shoppinglist.pop(2)

#hopefully this just reitirates the delicateness by which we have to use index values

#Removing by the .remove() function
#We can more safely remove by using the remove function
#let's first rebuild our shopping list
shoppinglist = ['apples',
                'oranges',
                'paper towels',
                'napkins',
                'hot dogs',
                'ketchup']

print("Our rebuilt shopping list is:")
print(shoppinglist)
print("Now we're going to remove one item: napkins")
shoppinglist.remove('napkins')
print("Here's the updated list after we revmoed napkins.")
print(shoppinglist)

#######################################
#SORTING:
#######################################
#We can also sort a list temporarily or permanently

#Temporary Sorting:
print("Shopping List temporarily sorted")
print(sorted(shoppinglist))

#Permanent Sorting:
print("Shopping List permanently sorted")
shoppinglist.sort()
print(shoppinglist)

#We can also reverse sort a list:
shoppinglist.reverse()
print("Now our shopping list should be sorted in reverse.")
print(shoppinglist)

#######################################
########   LENGTH of a List  ##########
#######################################

#Often we will need to find the number of items in an index. Or at least understand
#that this is an upper limit when we're trying to access an item in the list.
print("the number of items in our shopping list is:")
print(len(shoppinglist))

#based on the length of a list we can determine the max index value
#to access.  because lists are ZERO based it will always be len(list) - 1
#i.e.
print("the max index value we can access should always be:")
print(shoppinglist[len(shoppinglist) - 1])

#######################################
#######   Index Out of Range  #########
#######################################

#"Index out of range" is a common error when trying to access list items
#this is just because it is easy to inadverantly access a list item
#that doesn't exist.  for example:
print(shoppinglist[len(shoppinglist)])
#this will not work
#even though we are trying to use a property of the list (the length)
#to access an item in the list.  
