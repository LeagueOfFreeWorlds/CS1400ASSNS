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
        self.__NAME = name
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
        app1 = list(self.__NAME)
        app2 = list(other.getName())
        headR = (self.__HEAD_RADIUS + other.__getHeadRadius()) * 0.25
        bodyR = (self.__BODY_RADIUS + other.__getBodyRadius()) * 0.25
        bodyH = (self.__BODY_HEIGHT + other.__getBodyHeight()) * 0.125
        appf = []
        name = ''
        appf.append(app1)
        appf.append(app2)
        appfl = shuffle(appf)
        averageL = (len(app1) + len(app2)) // 2
        for i in range(averageL):
            if len(appfl) > i:
                name = ''.join(appfl[i])

        return Orbian(name, headR, bodyR, bodyH)

    def __len__(self):
        return self.getHeight()

    def __gt__(self, other):
        return self.getVolume() > other.getVolume()




