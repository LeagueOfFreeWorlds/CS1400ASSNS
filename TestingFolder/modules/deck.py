from modules.card import Card
import random
class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        for i in range(52):
            self.__deck.append(Card(i))
        random.shuffle(self.__deck)

    # Remember that pop with no parameter removes last item from the list, and also
    # returns it to the console.
    def draw(self):
        return self.__deck.pop()
