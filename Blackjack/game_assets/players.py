import random, time

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
        print(f"{self._name} start his/her turn.")
        time.sleep(2)

        while self.__in_game:
            # TODO check hand value
            hand_value = self.hand_value
            print(f"Cards: {self.hand}")
            print(f"Hand value: {hand_value}")
            time.sleep(2)

            if hand_value < 18:
                # call deck.draw()
                new_card = deck.draw()
                print(f"New card: {new_card}")
                self.__hand.append(new_card)
            else:
                print(f"{self._name} finishes his/her turn")
                self.__in_game = False
    
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
        # hand_value = 0
        # for card in self.__hand:
        #     hand_value += card.value

        # return hand_value

        return sum([card.value for card in self.__hand])

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
    ai_player.create()
    
    deck = Deck()
    ai_player.draw_card(deck)
    print(ai_player, ai_player.hand, ai_player.hand_value)