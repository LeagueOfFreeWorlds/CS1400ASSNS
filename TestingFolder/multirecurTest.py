lst = [[1, 2, 3], [4, 5, 6]]

for x in range(len(lst[0])):
    for y in range(len(lst)):
        print(lst[y][x], end=" ")
