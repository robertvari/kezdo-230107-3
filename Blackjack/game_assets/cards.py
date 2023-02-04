class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"

    def __repr__(self):
        return f"{self.__name}"


class Deck:
    def __init__(self):
        self.__cards = []

        self.create()

    def create(self):
        self.__cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]
        
    @property
    def cards(self):
        return self.__cards

    @property
    def card_number(self):
        return 0

if __name__ == "__main__":
    deck = Deck()
    deck.create()