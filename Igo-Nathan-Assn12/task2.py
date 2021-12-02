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
        inputValue = input("Enter a # value:\t")
        if inputValue == '':
            break
        else:
            inputList.append(inputValue)

    print(displayCalculations(inputList))



def displayCalculations(list):
    sum = sumVal(list)
    print("The length of the list is:\t" + str(len(list)))
    print("The maximum value in the array is:\t" + str(maxVal(list)))
    print("The minimum value in the array is:\t" + str(minVal(list, maxVal(list))))
    print("The sum of all values is:\t" + str(sum))
    print("The average value of the list is:\t" + str(avrg(list, sum)))

def maxVal(list):
    maximum = 0
    for i in list:
        if (int(i) > maximum):
            maximum = int(i)
    return int(maximum)

def minVal(list, smallest):
    for i in list:
        if int(i) < smallest:
            smallest = int(i)
    return smallest

def sumVal(list):
    sum = 0
    for i in list:
        sum += int(i)
    return sum

def avrg(list, sum):
    average = sum // (len(list) - 1)
    return average

main()
