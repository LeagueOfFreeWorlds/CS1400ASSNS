from modules.cardmap import SUITS
from modules.cardmap import RANKS

class Card:
    def __init__(self, id):
        self.__id = id

    def getRank(self):
        return RANKS[self.__id % 13]

    def getSuit(self):
        return SUITS[self.__id // 13]

    def __repr__(self):
        return self.getRank() + " of " + self.getSuit()
