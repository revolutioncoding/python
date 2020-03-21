"""
The Code Revolution
Lesson 10
Databases & Persistence
Part II
"""

"""
This exercise is more challenging because we are adding a Race Car
and a Driver.  That is two classes / objects we're dealing with.
But when we add the Race Car we are only going to reference the Drivers ID
in the DB.  So while Python understands that the Driver object
is part of the Race Car object, the Database doesn't work this way.
That is, we have to be more deliberate about adding these records in the DB.
This is another mini lesson on DBs.  Tables in the Database are related
to each other via keys.  Typically a table will have a Primary Key which
is a unique value for each record in the Database.  Any related table
will have a foreign key that is a reference to the primary key.  That is,
in our example the data in each table would look like:

Use the Sqlite GUI Tool we installed previously
to set up these.  Each setup will just generate the
SQL Table Create script (below) for you to run.

##### Drivers Table
CREATE TABLE Driver (
    ID        INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName  TEXT,
    DOB       TEXT,
    Victories INTEGER
);


##### Race Car Table
#####
This table has a Foreign Key which is equal to the Primary Key of the
Driver table.  That primarily means that in Python we need to
create the Driver record first, and then pass that Driver ID as the
Foreign Key value on the RaceCars table.
#####
CREATE TABLE RaceCars (
    Make     TEXT,
    Model    TEXT,
    Year     INTEGER,
    Mileage  REAL,
    RacesWon INTEGER,
    Driver   INTEGER REFERENCES Driver (ID) 
);
NOTE: How the Driver column indicates a reference to the
Driver (table) and the ID (column).
*When you add this Foreign Key column you'll specify that it is a
foreign key and you will then associate the ID column from the Driver table


"""
import sqlite3

##################################
## CREATE TABLE AND POPULATE #####
##################################
def checkfortables():

    conn = sqlite3.connect("kaman.db")
    #Create a cursor object which will allow us to interact with the database:
    c = conn.cursor()

    """
    This is just going to make sure you setup your tables correct
    
    """
    
    try:
        print("Checking on Racecars tables")
        c.execute("SELECT * FROM RaceCars")
        print("Congrats! Racecar table found")
    except sqlite3.Error as e:
        print("Error checking for Racecars table. Make sure it exists!")
        print(e) 


    try:
        print("Checking on Drivers tables")
        c.execute("SELECT * FROM Drivers")
        print("Congrats! Drivers table found")
    except sqlite3.Error as e:
        print("Error checking for Drivers table. Make sure it exists!")
        print(e) 
    
    #be sure to close the connection to the DB.  Often in programming you can
    #only have so many connections and once you max out, you application will fail
    #the way to resolve this is by closing your connections when you're done
    conn.close()
    
##################################
### SELECT / FETCH THE DATA  #####
##################################
def addracecaranddriver():
    print("Hello and welcome to the Code Revolution's")
    print("Race Car & Driver Management System - RCDMS!")
    print("Please enter:\n1. Enter a new driver\n2. Enter a new race car")
    print("Enter q to quit!")
    userchoice = ""
    while userchoice != "q":
        #because q is not an int, don't conver the input yet
        userchoice = input("=>")
        #since we're mixing strings with ints on the choices
        #we have to be careful not to create any conversion errors
        try:
            userchoice = int(userchoice)
        except:
            if userchoice == "q":
                break
        
        if userchoice == 1:
            enterdriver()
        elif userchoice == 2:
            enterracecar()
        
    print("Thank you for using the Code Revolution's RCDMS")
    

##################################
### SELECT / FETCH THE DATA  #####
##################################
def enterdriver():
    print("Here are the current drivers:")
    
    conn = sqlite3.connect("kaman.db")
    c = conn.cursor()
    
    count = 0
    for row in c.execute("SELECT * FROM Drivers"):
        print(row)
        count += 1
    
    print("Are you sure you want to add another?")
    userchoice = input("Yes/No?")
    if userchoice.upper() == "YES":
        firstname = input("Driver's First Name=> ")
        lastname = input("Driver's Last Name=> ")
        dob = input("Date of Birth=> ")
        #Use a try / except block to make sure they've entered the correct type
        try:
            victories = int(input("Number of Victories=> "))
        except:
            victories = 0
            print("Invalid value for # of victories.  Set to 0")

        
    driver = [count, firstname, lastname, dob, victories]
    
    
    #insert new record into DB
    #we'll use a try to avoid conversion errors
    try:
        c.execute("INSERT INTO Drivers VALUES (?, ?, ?, ?, ?)", driver)
        print("Record inserted successfully!")
    except sqlite3.Error as e:
        print("Error inserting new driver into DB")
        print(e)    
    
    #Don't forget to save / commit!!!
    conn.commit()
    
    #Don't forget to close your connection!!!
    conn.close()
    
    print("Would you like to return to the main menu?")
    navigation = input("Yes/No")
    if navigation.upper() == "YES":
        gotomain()

def enterracecar():
    print("Here are the current drivers:")
    print("Please select the driver to add your race car")
 
    
    conn = sqlite3.connect("kaman.db")
    c = conn.cursor()
    
    for row in c.execute("SELECT * FROM Drivers"):
        print(row)
    
    driver = int(input("=>"))
       
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    mileage = int(input("Enter race car mileage: "))
    raceswon = int(input("Enter the number of races won: "))
    
    racecar = [driver, make, model, year, mileage, raceswon]
    #insert new record into DB
    #we'll use a try to avoid conversion errors
    try:
        c.execute("INSERT INTO Racecars VALUES (?, ?, ?, ?, ?, ?)", racecar)
        print("Record inserted successfully!")
    except sqlite3.Error as e:
        print("Error inserting new race car into DB")
        print(e)    
    
    #Don't forget to save / commit!!!
    conn.commit()
    
    #Don't forget to close your connection!!!
    conn.close()
    
    print("Would you like to return to the main menu?")
    navigation = input("Yes/No: ")
    if navigation.upper() == "YES":
        gotomain()

    
###########################################
###########################################
def gotomain():
    print("Welcome to the Code Revolutions's DB Lesson!")
    print("Please select an option: \n1. Check for existence of RaceCars & Drivers tables\n2. Add Race Cars and Drivers")
    userchoice = int(input("=>"))
    if userchoice == 1:
        checkfortables()  #this
    elif userchoice == 2:
        addracecaranddriver()

#entry function
gotomain()