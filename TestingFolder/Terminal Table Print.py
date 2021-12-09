print("\t\t Table Program")


# Display table body:
for i in range(1, 9):
    print("| " + str(i) + " |", end=' ')
    for j in range(1, 9):
        if i == 1:
            print("| " + str(j) + " |", "|", end=' ')
        else:
            # Display the product aligned properly
            print("|   |", end=' ')
    print()
    print()
    print("------------------------------------------------------")
    print()
