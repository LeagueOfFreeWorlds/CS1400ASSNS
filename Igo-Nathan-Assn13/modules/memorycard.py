from random import randint
class MemoryCard:
    def __init__(self, id):
        self.__id = id
        self.__flipped = False

       # Returns true if face is currently turned up:
    def isFlipped(self):
        return self.__flipped


    # Returns value asso. with card:
    def getValue(self):
        value = ((self.__id) // 2) + ord('!')
        return chr(value)


    # Change card from face up to face down:
    def toggleFlipped(self):
        if self.isFlipped() == False:
            self.__flipped = True
        else:
            self.__flipped = False


   # Returns string asso. with whether face up (which it will print suit and rank), or face down (returns space).
    def displayCard(self):
        string = ''
        if self.isFlipped():
            string = str(self.getValue())
            return string
        else:
            string = ' '
            return string
