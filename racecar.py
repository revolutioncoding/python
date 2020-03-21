#The Code Revolution
#Race Car Class that inherits from Car

from car import Car
from driver import Driver

class RaceCar(Car):
    """
    This class represents a specific type of car that will
    have attributes specific to a race car but will inherit
    the attributes of the parent car class
    """

    def __init__(self, make, model, year, driver, raceswon):
        """
        Initialize attributes of the parent class
        """
        super().__init__(make, model, year)

        """
        Add sub class specific attributes
        """
        self.driver = driver
        self.raceswon = raceswon


    def age(self):
        """
        We are going to override this method becaues the age of a race car
        is very different than the age of a car
        """
        print("I am a race car, my parts are constantly replaced.")
        print("And my body, frame and chassis is constantly cut and welded.")
