from card import Card
from random import shuffle


class Deck:
    # Since each object will not have a different property, we defined it as a class variable.
    cardTypes = ["diamonds", "clubs", "hearts", "spade"]
    cardValues = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(cardType, cardValue) for cardType in Deck.cardTypes for cardValue in Deck.cardValues]

    def countCard(self):
        return len(self.cards)

    def shuffleCards(self):
        if self.countCard() < 52:
            raise ValueError("You can shuffle the cards without breaking the deck.")
        shuffle(self.cards)

    def dealCards(self, piece):
        count_card = self.countCard()
        if count_card == 0:
            raise ValueError("All cards are dealt.")
        piece = min([count_card, piece])
        cards = self.cards[-piece:]
        self.cards = self.cards[:-piece]
        return cards

    def throwCard(self):
        return self.dealCards(1)[0]


deck = Deck()
