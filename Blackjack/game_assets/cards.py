import random

class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value
    
    def change_value(self):
        self.__value = 1

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

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card_data in cards:
                new_card = Card(f"{name} {card_data[0]}", card_data[1])
                self.__cards.append(new_card)

        random.shuffle(self.__cards)

    def draw(self):
        if len(self.__cards) == 0:
            print("There is no cards left in the deck. Create a new deck first!")
            return
        
        return self.__cards.pop(0)

    @property
    def cards(self):
        return self.__cards

    @property
    def card_number(self):
        return len(self.__cards)

if __name__ == "__main__":
    deck = Deck()

    for _ in range(60):
        my_card = deck.draw()
        print(my_card)
        print(deck.card_number)