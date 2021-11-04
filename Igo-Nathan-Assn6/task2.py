'''
@author: Nathan Igo
CS1400
Program creates a simulation of 100,000 nights that elephants enter a pen and a zookeeper 
randomly checks pens for whether or not they are occupied.
'''
from random import randint
NUM_OF_NIGHTS = 100000
totalGuesses = 0
correctGuesses = 0
twoE = 0

continueLoop = "yes"
while continueLoop == "yes" or continueLoop == "y" or continueLoop == "Y" or continueLoop == "YES":
    #For-loop generates full array for nights that pens are occupied by one elephant:
    for i in range(1, NUM_OF_NIGHTS):
        E1 = randint(1, 6)
        E2 = randint(1, 6)
        zGuess = randint(1, 6)
        if zGuess == E1 and zGuess == E2:
            correctGuesses +=1
            twoE +=1
        elif zGuess == E1 or zGuess == E2:
            correctGuesses +=1
        totalGuesses +=1
    percentageCorrect = (correctGuesses / totalGuesses) * 100
    twoElephantsPresent = (twoE / totalGuesses) * 100
    pResult = format(percentageCorrect, "3.2f")
    twopResult = format(twoElephantsPresent, "3.2f")
    print("The zookeeper has a " + str(pResult) + "% chance of randomly selecting a pen\n that has at least one elephant present.")
    print("The zookeeper has a " + str(twopResult) + "% chance of randomly selecting a pen\n that has two elephants present.")
    continueLoop = input("Do you wish to re-run the simulation? (Y/n)?  ")