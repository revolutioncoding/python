"""
The Code Revolution
Lesson 10
Databases & Persistence
"""

"""
Today we introduce the concept of persistence.  Persistence implies storage.  So far our
data, our variables, only exsist in the memory of our computer.  Specifically they only
exist in the lifetime of our Shell window.  Once we close the shell the data is gone.
This is a common problem in programming.  We need a way to store data when the computer is
off or the program is closed.  And then consequently we need to be able to acces that
information.  We can do this by using files.  However we are skipping the lesson files
because we feel Databases are a more important concept to grasp.  And Databases store the data
in files.  But we don't have to worry about the specific mechanics of the file.  We just
have to know how to interact with the Database, and the database will store create and manage
the files.  This lesson introduces SQLite which is a light weight database that comes
installed with Python.
"""



"""
Now we are going to create our objects as tables so we can store data in the database
"""
import sqlite3

##################################
## CREATE TABLE AND POPULATE #####
##################################
def createandpopulate():

    conn = sqlite3.connect("kaman.db")
    #Create a cursor object which will allow us to interact with the database:
    c = conn.cursor()

    """
    The text below inside the c.execute() function is SQL.
    SQL stands for Structured Query Language and it is pretty standard across
    all traditional Database Management Systems (DBMS).  There are some
    variations between Oracle, MS SQL Server, MYSQL, etc.  But generally
    and as compared to programming languages it is still all SQL.  Being familiar
    with SQL is pretty critical to interacting with databases.  We can actually
    execute SQL inside a DB GUI. In this lesson we will use SQLite Studio.
    """
    #The create the table based on the car object
    # Create table
    c.execute('''CREATE TABLE cars
                 (make text, model text, year real, mileage real)''')

    
    # Insert a car instance into the new table
    c.execute("INSERT INTO cars VALUES ('ford','mustang', 2019, 200.3)")
    c.execute("INSERT INTO cars VALUES ('chevy','camaro', 2012, 10210.9)")
    c.execute("INSERT INTO cars VALUES ('nissan','300zx', 1999, 5580.0)")


    # With Databases we generally have to commmit the data / command or else it won't save
    conn.commit()
    
    #be sure to close the connection to the DB.  Often in programming you can
    #only have so many connections and once you max out, you application will fail
    #the way to resolve this is by closing your connections when you're done
    conn.close()

##################################
### SELECT / FETCH THE DATA  #####
##################################
def getcarsfromDB():
    # Now we'll want to select the data from the database and print it out to our shell
    # so we can confirm that we entered data correctly
    
    #there is some 'natural' code repitition here
    conn = sqlite3.connect("kaman.db")
    c = conn.cursor()
    
    for row in c.execute("SELECT * FROM cars"):
        print(row)
        
        
    #let's not forget to the close the connection
    conn.close()
 
##################################
### SELECT / FETCH THE DATA  #####
##################################
def addnewcar():
    print("Hello and welcome to the Code Revolution's")
    print("Car Registration System!")
    print("Please enter your Car's Details Below:")
    usermake = input("Make=> ")
    usermodel = input("Model=> ")
    #Remember the try / except blocks allow us to anticipate user errors
    #and course correct. This is likely when excpeting an integer value.
    #Strings will generate errors especially at the DB level if we try to
    #insert a string into a number formatted column.
    try:
        useryear = int(input("Year=> "))
    except:
        print("Invalid mileage!")
        useryear = 1900
    #
    try:
        usermileage = int(input("Mileage=> "))
    except:
        print("Invalid Mileage!")
        usermileage = 0
        
    carlist = [usermake, usermodel, useryear, usermileage]
        
    ##### Now Connect to the Database and add the new user's car record #####
    conn = sqlite3.connect("kaman.db")
    #create the cursor object to interact with the DB
    c = conn.cursor()
    
    #insert new record into DB
    #we'll use a try to avoid conversion errors
    try:
        c.execute("INSERT INTO cars VALUES (?, ?, ?, ?)", carlist)
        print("Record inserted successfully!")
    except sqlite3.Error as e:
        print("Error inserting new car into DB")
        print(e)    
    
    #Don't forget to save / commit!!!
    conn.commit()
    
    #Don't forget to close your connection!!!
    conn.close()
    
###################################################
###################################################
    
print("Welcome to the Code Revolutions's DB Lesson!")
print("Please select an option: \n1. Create a cars table and populate it. \n2. Select and Print all Rows from cars table")
print("3. Enter your own car into the DB")
userchoice = int(input("=>"))
if userchoice == 1:
    createandpopulate()
elif userchoice == 2:
    getcarsfromDB()
elif userchoice == 3:
    addnewcar()

    