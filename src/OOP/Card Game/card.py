class Card:
    def __init__(self, cardType, cardValue):
        self.cardType = cardType
        self.cardValue = cardValue

    # represent the instance
    def __repr__(self):
        return f"{self.cardType} - {self.cardValue}"

