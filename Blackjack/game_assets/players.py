import random, time

class Player_Base:
    def __init__(self):
        self._name = None
        self.__credits = 0
        self._hand = []
        self._in_game = True
    
    def create(self):
        self.__credits = random.randint(1, 20)
        self._name = self.__get_random_name()

    def give_bet(self, value):
        if value > self.__credits:
            print(f"{self._name} hans no more credits to play :(")
            self._in_game = False
            return
        
        self.__credits -= value
        return value

    def reward(self, value):
        self.__credits += value

    def start_hand(self, deck):
        print(f"{self._name} draw start hand.")
        self._hand.clear()
        self._in_game = True

        self._hand.append(deck.draw())
        self._hand.append(deck.draw())

    def has_credits(self, value):
        return self.__credits >= value

    def draw_card(self, deck):
        print(f"{self._name} start his/her turn.")
        time.sleep(1)

        while self._in_game:
            # check hand value
            hand_value = self.hand_value

            if hand_value < 18:
                # call deck.draw()
                new_card = deck.draw()

                # if we draw and Ace and we had a hand value > 10
                if hand_value > 10 and new_card.value == 11:
                    new_card.change_value()

                self._hand.append(new_card)
            else:
                print(f"{self._name} finishes his/her turn")
                self._in_game = False
    
    @property
    def hand(self):
        return self._hand

    def reveal_hand(self):
        print(f"{self._name} hand: {self.hand}. Hand value: {self.hand_value}")

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
        # for card in self._hand:
        #     hand_value += card.value

        # return hand_value

        return sum([card.value for card in self._hand])

    def __str__(self) -> str:
        return str(self._name)

    def __repr__(self) -> str:
        return str(self._name)

class Player(Player_Base):
    def create(self): # method override
        super().create()
        # self._name = input("What is your name?")
        self._name = "Robert Vari"

    def draw_card(self, deck):  # we override the Base class draw_card method
        print(f"This is your turn {self._name}")
        while self._in_game:
            print(f"Your hand: {self.hand}. Hand value: {self.hand_value}")
            
            if self.hand_value > 21:
                print(f"You hand value is {self.hand_value}. You lost this turn :(")
                self._in_game = False
                break
            
            player_input = input("Do you want ot draw a card? (y/n)")
            if player_input == "y":
                new_card = deck.draw()
                print(f"Your new card: {new_card}")
                self._hand.append(new_card)
            else:
                self._in_game = False


class AIPlayer(Player_Base):
    pass


if __name__ == "__main__":
    from cards import Deck
    deck = Deck()

    player = Player()
    player.create()

    ai_player = AIPlayer()
    ai_player.create()

    player.start_hand(deck)
    player.draw_card(deck)

    ai_player.start_hand(deck)
    ai_player.draw_card(deck)

    print("-"*50, "Game Results", "-"*50)
    print(player, player.hand, player.hand_value)
    print(ai_player, ai_player.hand, ai_player.hand_value)