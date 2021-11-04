'''
@author: Nathan Igo
CS-1400
'''
import random
runAgain = "yes"
# Function that takes user input and prints pyramid to console:
def pyramidGenerator(xRow):
    # spacing calculation determines number of spaces needed at the top in order to fit rows at the very end:
    spacing = 2*xRow - 2
    # Because of two digits, spacing needs to address increased integer space for digits >=10, thus 'tencing.'
    tencing = 2*xRow - 18
    # i is representative of the number values for within the pyramid.
    for i in range (xRow + 1):
        if i <= 9:
            # for loop indents the pyramid based of spacing calculation:
            for indentation in range(0, spacing):
                print(end=" ")
            spacing = spacing - 1
            # Prints numbers to the display:
            for numbers in range(0, i):
                print(i, end=" ")
        elif i > 9:
            # Because of bigger digits, use the tencing space instead:
            for tendentation in range (0, tencing):
                print(end=" ")
            tencing = tencing - 1
            for tenbers in range(0, i):
                print(i, end=" ")
        print("\r")


# Program will continue to run, until user wishes to end the program by typing anything other than what
# the while loop classifies:
while runAgain == "yes" or runAgain == "y" or runAgain == "Y" or runAgain == "Yes" or runAgain == "":
    rowInput = eval(input("Enter number of rows you want your pyramid to have:  "))
    pyramidGenerator(rowInput)
    runAgain = input("Would you like to run program again? (Y/n):   ")
