'''
@Author:Nathan Igo
@Date: 11/30/2021
CS-1400
'''

def main():
    baseList = list(range(1, 101))
    # list1 - Index of all even numbers in baseList:
    list1 = [i for i in baseList if i % 2 == 0]
    print(list1)
    # list2 - Index of all multiples of 3 that are <50 in baseList:
    list2 = [i for i in baseList if i % 3 == 0 and i < 50]
    print(list2)
    # list3 - Index of all values that are 10x greater than # from baseList that are multiples of 5
    # and greater than 20:
    list3 = [i*10 for i in baseList if i % 5 == 0]
    print(list3)

main()
