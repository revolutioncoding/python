#The Code Revolution
#Lesson 06
#Dictionaries & 'Bonus' Functions!

# In this lesson we are going to define some functions.  In Python these
# functions have to live at the top of our code file in order
# that they are in "scope".  I.e. such that they exist when we try to call / reference them.
# The exercise is otherwise simple:
# 1. Create a set of print statements asking the user (you the coder) to chose their exercise
# 2. For each exercise we will create a function and insert our code within that function
# 3. Therefore each time we run our file we will only have to review that code and not the entire file
# 4. But much like a real program all of our code is in one file.
# It's just that only the parts we need will run

#Example 1
#Our first function
#Simple "Alien" Dictionary:
def simple_alien_dictionary():
    alien = {'color': 'green', 'points': 5}
    alien_key = "color"
    print(alien_key + ": " + str(alien[alien_key])) #this str conversion here is just to be safe
    alien_key = "points"
    print(alien_key + ": " + str(alien[alien_key]))

#Example 2
#Full Alien Dictionary
def full_alien_dictionary():    
    #Start with an empty Dictionary
    alien = {}

    #Add key/values:
    alien['color'] = 'green'
    alien['points'] = 5
    alien['x_position'] = 0
    alien['y_position'] = 25
    alien['speed'] = 'medium'


    print(alien)
    print("The speed of the alien is: " + alien['speed'])
    print("The points for the alien is: " + str(alien['points']))


    alien['home_planet'] = 'Kodos'
    print("Alien key-values before deletion")
    print(alien)
    del alien['home_planet']
    print("Alien key-values after deletion")
    print(alien)

#Example 3
#People and their favorite programming languges
def peoples_favorite_coding():

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'c#'
        }

    #Loop through languages and print each one
    for person, language in favorite_languages.items():
        print("\nPerson:" + person)
        print("Language: " + language)

    #just to clean up the output
    print("\n\n")

    #Make another loop, but make it prettier
    for person, language in favorite_languages.items():
        print(person.title() + "'s favorite language is: " + language.title())

    #just to clean up the output
    print("\n\n")

    #Looping through keys
    friends = ['jen', 'sarah']
    for name in favorite_languages.keys():
        print(name.title())

        if name in friends:
            print("Hi " + name.title() + ", I see your favorite language is " +
                favorite_languages[name].title() + "!")


    #using not in boolean check & searching
    name_search = input("What name do you want to check?")
    if name_search not in favorite_languages.keys():
        print(name_search + " needs to enter their favorite language!")
    else:
        print(name_search + "'s favorite language is: " + favorite_languages[name_search])


    print("\n\n")
    #Sorting a Dictionary
    for name in sorted(favorite_languages.keys()):
        print(name.title() + ", thank you for taking the poll!")

#Example 4
#List of Dictionaries
def list_of_dictionaries():
    #Create more than one Dictionary and then a List of Dictionaries
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}

    #create the list
    aliens = [alien_0, alien_1, alien_2]

    for alien in aliens:
        print(alien)

#Example 5
#Dynamically Build a list of 30 Aliens
def dynamically_build_aliens():
    #Dynamically build the aliens
    aliens = []

    #make 30 green aliens
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    #print the first five aliens
    print("We're about to print the first five aliens")
    #not the for loop below can also be written as:
    #for alien in aliens[0:5]:
    for alien in aliens[:5]:
        print(alien)
    print("...")

    #show how many aliens have been created
    print("The total number of aliens created is: " + str(len(aliens)))

    #Dynamically build the aliens and change the properties based on the item mod
    aliens = []

    #make 30 green aliens
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        if alien_number % 2 != 1:
            new_alien["color"] = 'yellow'
        
        aliens.append(new_alien)

    #reprint the aliens and see if the yellows got added
    for alien in aliens:
        print(alien)

    
#Example 6
#A List in a Dictionary
def list_in_dictionary():
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
        }
    #Now print out your pizza, looping through the toppings separately
    print("You ordered a " + pizza['crust'] + " crust pizza with the following toppings: ")
    #Now loop through toppings and print each topping:
    for topping in pizza["toppings"]:
        print("\t" + topping) #the '\t' switch adds a tab character to the output

#Example 6
#List inside of a Dictionary
#You can nests lists as a dictionary's value associated to its key when you
#want to store more than one value with each key
#for example, see the Dictionary below of best selling cars by origin country:
def list_in_dictionary():
    top_cars = {
        "Germany" : ["BMW", "Audi"],
        "USA": ["Ford", "Chevrolet", "Jeep"],
        "Japan": ["Toyota", "Honda"]
        }

    #print the lists out for each country
    for country, cars in top_cars.items():
        print("\n" + country.title() + "'s top cars are:")
        for car in cars:
            print("\t" + car.title())

#Example 7
#Dictionary inside of a Dictionary
#We can also store dictionaries inside of dictionaries
#But like many things this is better to see in practice and through examples
def dictionary_in_dictionary():
    ballers = {
        "messi": {
            "first": "leo",
            "last": "messi",
            "team": "barca"
            },
        "cr7": {
            "first": "christian",
            "last": "ronaldo",
            "team": "juventus"
            }
        }

    #we have created a dictionary of soccer players where
    #each player value is another dictionary
    #now we want to iterate through these players and print the results
    for player, player_info in ballers.items():
        print("Baller nickname: " + player)
        print("\tFirst Name: " + player_info['first'].title())
        print("\tLast Name: " + player_info['last'].title())
        print("\tCurrent Club: " + player_info['team'].title())
###########################################################################################
##      This is the beginning of our program because it's where our code actually        ##
##      tries to interact with the user and then based on your selection will call       ## 
##      the relevant exercises we have built into each fuction "above"                   ##
###########################################################################################
    
print("Welcome to the Code Revolution Lesson 6 Dictionaries and Functions!")
print("Please choose a lesson to call that function.")
print("To implement this function you will have to add the relevant function call and/or code.")
print(" 1: Simple Alien Dictionary \n 2: Full Alien Dictionary \n 3: People and their favorite languages")
print(" 4: Create a List of Dictionaries \n 5: Dynamically build 30 Aliens \n ")
print(" 6: List in a Dictionary \n 7: Dictionary in a Dictionary")
answer = input()

print("You chose: " + answer)
if answer == "1":
    simple_alien_dictionary()
elif answer == "2":
    full_alien_dictionary()
elif answer == "3":
    peoples_favorite_coding()
elif answer == "4":
    list_of_dictionaries()
elif answer == "5":
    dynamic_aliens()
elif answer == "6":
    list_in_dictionary()
elif answer == "7":
    dictionary_in_dictionary()







