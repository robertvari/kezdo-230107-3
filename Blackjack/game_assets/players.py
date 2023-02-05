import random

class Player_Base:
    def __init__(self):
        self._name = None
        self.__credits = 0
        self.__hand = []
        self.__in_game = True
    
    def create(self):
        self.__credits = random.randint(10, 100)
        self._name = self.__get_random_name()

    def draw_card(self, deck):
        # call deck.draw()
        new_card = deck.draw()
        
        # append new card to self.__hand
        self.__hand.append(new_card)
    
    @property
    def hand(self):
        return self.__hand

    def __get_random_name(self):
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"
    
    @property
    def credits(self):
        return self.__credits

    @property
    def hand_value(self):
        hand_value = 0
        for card in self.__hand:
            hand_value += card.value

        return hand_value

    def __str__(self) -> str:
        return str(self._name)


class Player(Player_Base):
    def create(self): # method override
        super().create()
        # self._name = input("What is your name?")
        self._name = "Robert Vari"


class AIPlayer(Player_Base):
    pass


if __name__ == "__main__":
    from cards import Deck

    ai_player = AIPlayer()
    deck = Deck()

    for _ in range(10):
        ai_player.draw_card(deck)
        print(ai_player.hand)
        print(ai_player.hand_value)