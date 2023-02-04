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


if __name__ == "__main__":
    card1 = Card("Spade 10", 10)