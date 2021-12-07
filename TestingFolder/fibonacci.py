def main():
    value = eval(input("Enter a value:\t"))
    print("The fibonacci of " + str(value) + " is " + str(fibonacci(value)))

def fibonacci(n):
    print("fibonacci (" + str(n) + ")")
    if n == 0:
        return 0
    elif == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

main()
