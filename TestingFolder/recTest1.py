# Recursion Test 1

def sampleFunction(value):
    if value == 0:
        return 1
    else:
        return sampleFunction(value)

print(sampleFunction(5))
