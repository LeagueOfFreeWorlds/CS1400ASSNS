import random
numList = []
for i in range(20):
   numList.append(random.randint(0, 40)) 

print(numList)
print(binarySearch(numList, key))


def binarySearchRecursiveHelper(numList, key, low, high):
    print("Recursive call:\t" + str(low) + " , " + str(high))
	if low > high:
		return -1
	# Found what we're looking for:
	mid = (low + high) // 2
	if key == numList[mid]:
		return mid
	# Thing we're looking for comes before the middle:
	elif key < numList[mid]:
		return binarySearchRecursiveHelper(numList, key, low, mid - 1)
	else:
		return binarySearchRecursiveHelper(numList, key, low, high)
	
def binarySearch(inputList, key):
	low = 0
	high = len(inputList) - 1
	return binarySearchRecursiveHelper(inputList, key, mid + 1, high)
