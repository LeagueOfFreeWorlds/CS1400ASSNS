from random import shuffle

# Returns a string of the board matrix for display:
class MemoryBoard:
    def __init__(self, rows, columns):
        self.__columns = columns
        self.__rows = rows
        self.__board = []

    def getBoard(self):
        letter = '!'
        letterList = []
        for i in range(self.__rows):
            self.__board.append([])
            for j in range(self.__columns):
                letterList.append(letter)
                shuffle(letterList)
                self.__board[i].append(letterList[i])
                letter = chr(ord(letter) + 1)
        string = ''
        for i in range(self.__rows):
            for j in range(self.__columns):
                if self.__board[i][j] == 'z':
                    string += str(self.__board[i][j])
                else:
                    string += ' '
                string += ' | '
            string += '\n'
            string += '--------------------------------\n'
        return string


    # Changes the value on the selected matrix.
    def flipCard(self, xAx, yAx):
        self.__board[xAx][yAx] = 'a'
        self.getBoard()


    # Quick check to determine if the card has already been flipped:
    ## TBD - Please go back to this:
    def isCardFlipped(self, xAx, yAx):
        if self.__board[xAx][yAx] != ' ':
            return True
        else:
            return False
    ## TBD - Please go back to this:
    def isMatch(self, pos1, pos2):
        if self.__board[pos1] == board[pos2]:
            return True
        else:
         return False


