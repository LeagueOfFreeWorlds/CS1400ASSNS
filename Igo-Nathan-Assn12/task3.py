from modules.deck import Deck
from time import sleep
def main():
    deck = Deck()
    isRunning = True
    dealerHand = []
    while isRunning:
        dealerAmount = int(input("How many cards do you wish to be dealt?\t"))
        print("Shuffling Deck:\t")
        thinking()
        for i in range(dealerAmount):
            dealerHand.append(deck.draw())
        print(dealerHand)
        runAgain = input("Would you like the dealer to reshuffle? (Y/n):\t")
        if runAgain == "N" or runAgain == "n" or runAgain == "no" or runAgain == "NO" or runAgain == "No":
            isRunning = False

    print("Thanks for playing!")
# Loading animation:
def thinking():
    for i in range(10):
        print(".", end="")
        sleep(0.5)
    print()

main()
