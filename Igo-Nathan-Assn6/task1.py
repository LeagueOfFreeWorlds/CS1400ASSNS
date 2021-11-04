'''
@author: Nathan Igo
CS1400
Fluky number generator that generates random numbers based on factors of 10. 
The program generates 10,000 random values between 0 and 10, including 0 and 10, 
and tries to find values that have one of the factors of 10 (2, and 5).
'''

import random
flukeCount = 0
# Arrays used for recalling generated seeds:
arr1 = []
resultArray=[]
while len(resultArray) != 7:
    # Function below generates our random numbers:
    random.seed(7)
    for i in range(1, 10001):
        randFluke = random.randint(0, 10)
        # Adding randomly generated array of values
        if (randFluke % 2) == 0 or (randFluke % 5) == 0:
            arr1.insert(i, randFluke)
            flukeCount+=1
    # Function below removes redundant values: 
    for value in arr1:
        if value not in resultArray:
            resultArray.append(value)
    print("Original array: ")
    print(arr1)
    print("Simplified array: ")
    print(resultArray)
    
print("Number of iterations to find fluky numbers:  " + str(flukeCount))