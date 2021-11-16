from modules.deck import Deck
def main():
    deck = Deck()

    dealerHand = []
    playerHand = []

    for i in range(5):
        playerHand.append(deck.draw())
        dealerHand.append(deck.draw())

    print(playerHand)
    print(dealerHand)
main()
