# Here I shall be testing ze values of list.
list = [2, 80, 9, 12, 308, 108, 48, 759, 5]
currMinIndex = 0
for i in range(len(list) -1):
    currMinIndex = i
    for j in range (i + 1, len(list)):
        if list[currMinIndex] > list[i]:
            currMinIndex = j

    if currMinIndex != i:
        list[i], list[currMinInex] = list[currMinIndex], list[i] 
print(list)
