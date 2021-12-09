class GameBoard:
    def __init__(self, columns, rows):
        self.__columns = columns
        self.__rows = rows

    def getBoard(self):
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

    def flipCard(self, x, y):
        self.__columns = y
        self.__rows = x
        self.getBoard()

    def isCardFlipped(self):

    isMatch(self, pos1, pos2):


