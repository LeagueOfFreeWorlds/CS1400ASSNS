from modules.cardmap import Title
from modules.cardmap import Gang
class Card:
    def __init__(self, id):
        self.__id = id

    def getTitle(self):
        return Title[self.__id % 17]

    def getGang(self):
        return Gang[self.__id // 17]

    def __repr__(self):
        return self.getTitle() + " Of " + self.getGang()
