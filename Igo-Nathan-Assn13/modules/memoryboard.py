from random import shuffle

# Returns a string of the board matrix for display:
class MemoryBoard:
    def __init__(self, rows, columns):
        self.__columns = columns
        self.__rows = rows
        self.__userSelection = ''
        self.__flippedLocation = []
        self.__board = []
        self.createBoard()

    def createBoard(self):
        letter = '!'
        letterList = []
        for i in range(self.__rows):
            self.__board.append([])
            for j in range(self.__columns):
                letterList.append(letter)
                shuffle(letterList)
                self.__board[i].append(letterList[i])
                letter = chr(ord(letter) + 1)

    def getBoard(self):
        string = ''
        for i in range(self.__rows):
            for j in range(self.__columns):
                if str(self.__board[i][j]) == self.__userSelection:
                    string += str(self.__board[i][j])
                else:
                    string += ' '

                string += ' | '
            string += '\n'
            string += '--------------------------------\n'
        return string


    # Changes the value on the selected matrix.
    def flipCard(self, xAx, yAx):
        self.__userSelection = self.__board[xAx][yAx]
        if self.isCardFlipped(xAx, yAx):
            self.__userSelection = 'A'
            self.getBoard()
        else:
            self.getBoard()


    # Quick check to determine if the card has already been flipped:
    def isCardFlipped(self, xAx, yAx):
        if self.__board[xAx][yAx] != ' ':
            return False
        else:
            return True
    def isMatch(self, pos1, pos2):
        if self.__board[pos1] == self.__board[pos2]:
            return True
        else:
         return False


