arr = [["|   |" for i in range(8)] for i in range(8)]

num = iter(range(1, 9))
colNum = iter(range(1, 9))

print(next(colNum), end=' ')
print()
for i in arr:
    print(next(num), end = ' ')
    print(' '.join(i))
