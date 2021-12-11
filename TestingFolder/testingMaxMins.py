from random import randint
lst = []

for i in range(20):
    lst.append(randint(1, 100))
print(lst)

def avrg(list, sum):
    average = ((len(list) - 1) - sum)
    return average

