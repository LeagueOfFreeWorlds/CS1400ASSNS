from time import time
from math import pi
class Blobber:
    # Constructor:
    def __init__(self, name, color, radius, height):
        self.baseTime = time
        self.__alive = True
        self.__name = name
        self.__color = color
        self.__radius = radius
        self.__height = height
        self.__health = pi * (self.__radius ** 2) * self.__height
        self.__hStat = 0
        ##############################################
        # The timer method changes the status of the blobber as it
        # continues to live.
    def getBlobberLifeTimer(self):
        return time() - self.baseTime
    # Returns tuple for vitalsOK:
    def vitalsOK(self):
        return self.__hpStat(), self.__alive
#################################################
    def dispName(self):
        return self.__name
    def setBlobName(self, name):
        self.__name = name
    def displayCol(self):
        return self.__color
    def changeColor(self, color):
        self.__color = color
    def hDecrement(self):
        while True:
            if (self.baseTime % 1 == 0):
                self.blobHealth()
    ## The blob Health decrements every second based on hDecrement
    def blobHealth(self):
        self.__hStat = self.__health - (self.__health * 0.002)
        self.__hpStat = (self.__hStat / self.__health) * 100
        if (self.__hStat < (self.__health * 0.9) or self.__hStat > (self.__health * 1.1)):
            self.__alive = False
    def feedBlobber(self, food):
        self.__radius = self.__radius + food
    def blobberSpeak(self):
        print("My name is " + self.__name + ", and I am " + self.__color)
        print("My current happiness is" + format(self.__hpStat, ".2%"))



