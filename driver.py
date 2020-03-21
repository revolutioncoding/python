#The Code Revolution
#Lesson 09 - Classes
#Driver Class

class Driver():
    
    
    """
    We will use this object to store more details about the driver and use
    that information within the RaceCar class
    """
    
    def __init__(self, firstname, lastname, DOB, victories):
        """"
        Initialize the attributes of the Driver class
        We *could* create a Person class and then inherit the Drive from that class but...
        we have to balance formality with need
        """
        self.firstname = firstname
        self.lastname = lastname
        self.DOB = DOB #this will just be a string "MM/DD/YYYY" for now
        self.victories = victories
        
    def ticker(self):
        print("Your driver is: "
              + self.firstname.title() + " "
              + self.lastname.title()
              + " has won "
              + str(self.victories)
              + " titles.")