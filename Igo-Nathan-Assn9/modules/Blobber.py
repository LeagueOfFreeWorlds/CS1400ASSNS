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
        self.__health = pi * (radius ** 2) * height
        self.__hStat = 0
        ##############################################
        # The timer method changes the status of the blobber as it
        # continues to live.
    def getBlobberLifeTimer(self):
        return time() -self.baseTime
    # Returns tuple for vitalsOK:
    def vitalsOK(self):
        return self.__hStat(), self.__alive
#################################################
    def displayName(self):
        return self.__name
    def setBlobName(self):
        nameSet = eval(input("Enter a new name: "))
        self.__name = nameSet
    def displayColor(self):
        return self.__color
    def changeColor(self):
        colorSet = eval(input("Enter a new color:    "))
        self.__color = colorSet
    def hDecrement(self):
        while True:
            if (self.baseTime % 1 == 0):
                self.blobHealth()
    ## The blob Health decrements every second based on hDecrement
    def blobHealth(self):
        self.__hStat = self.__health - (self.__health * 0.002)
        if (self.__hStat < (self.__health * 0.9) or self.__hStat > (self.__health * 1.1)):
            self.__alive = False
    def feedBlobber(self):

    def blobberSpeak(self):



