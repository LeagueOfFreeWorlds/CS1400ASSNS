from math import pi
from random import shuffle # Hint hint
from random import randint
import time

class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name.capitalize()
        self.__BIRTH_TIME = time.time()

        # This is the only variable
        self.__adult = False
    # Methods:
    def getName(self):
        return self.__NAME

    def getVolume(self):
        return int(self.__getHeadVolume() * self.__getBodyVolume())

    def getHeight(self):
        return self.__getBodyHeight() + (self.__getHeadRadius()) * 2

    def getAge(self):
        return int((time.time() - self.__BIRTH_TIME) / 5)

    def adulting(self):
        if self.getAge() >= 2:
            self.__HEAD_RADIUS * 2
            self.__BODY_RADIUS * 2
            self.__BODY_HEIGHT * 4
        return Orbian()

    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3

    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()

    def __getHeadRadius(self):
        return self.__BODY_RADIUS

    def __getBodyRadius(self):
        return self.__BODY_RADIUS
    def __getBodyHeight(self):
        return self.__BODY_HEIGHT
    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            self.__adult = True

    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND OTHER STARTER CODE FOR INSIGHT ######
    # Dunders:
    def __add__(self, other):
        app = list(self.__NAME + other.getName())
        #app2 = list(other.getName())
        #l = app1, app2
        shuffle(app)
        headR = int((self.__HEAD_RADIUS + other.__getHeadRadius()) * 0.25)
        bodyR = int((self.__BODY_RADIUS + other.__getBodyRadius()) * 0.25)
        bodyH = int((self.__BODY_HEIGHT + other.__getBodyHeight()) * 0.125)
        name = ''
        averageL = (len(self.__NAME + other.getName())) // 2
        for x in range(averageL):
            name += app[x]
        name.capitalize()
        return Orbian(name, headR, bodyR, bodyH)

    def __sub__(self):
        return None
    def __len__(self):
        return self.getHeight()

    def __gt__(self, other):
        return self.getVolume() > other.getVolume()




