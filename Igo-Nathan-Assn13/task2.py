from random import randint
# Remember how to use this kind of variable?
count = 0

def main():
    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)

    numPos = binarySearch(numList, key)

    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))

def aggienacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * (aggienacci(n - 3) + aggienacci(n - 2)) / aggienacci(n - 1)

def binarySearch(nL, key):
    global count
    low = 0
    high = len(nL) - 1
    while high >= low:
        count += 1
        mid = (high + low) // 2
        print(nL[low:high + 1])
        if key == nL[mid]:
            return mid
        elif key < nL[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print("Count:\t" + str(count))
    return -1



main()

