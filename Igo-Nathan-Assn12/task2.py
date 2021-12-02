'''
@Author:Nathan Igo
@Date:  12/1/2021
CS-1400
'''
def main():
    enterPressed = False
    inputList = []
    print("Welcome. Please enter values into the terminal to populate a list for calculation.")
    print("Hit ENTER once you are satisfied with the amount of data you've provided.")
    while enterPressed != True:
        inputValue = int(input("Enter a # value:\t"))
        if inputValue == '':
            break
        else:
            inputList.append(inputValue)

    print(displayCalculations(inputValue))

main()

def displayCalculations(list):
    print("The length of the list is:\t" + str(len(list)))
    print("The maximum value in the array is:\t" + maxVal(list))
    print("The minimum value in the array is:\t" + minVal(list))
    print("The sum of all values is:\t" + sumVal(list))
    print("The average value of the list is:\t" + avrg(list))
def maxVal(list):
    maximum = 0
    for i in list:
        if (i > maximum):
            maximum = i
    return maximum
def minVal(list):
    minimum = 0
    for i in range(list):
        if
