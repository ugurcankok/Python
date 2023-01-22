from card import Card


class Deck:
    # Since each object will not have a different property, we defined it as a class variable.
    cardTypes = ["diamonds", "clubs", "hearts", "spade"]
    cardValues = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(cardType, cardValue) for cardType in Deck.cardTypes for cardValue in Deck.cardValues]


deck = Deck()
