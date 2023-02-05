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

    def __get_random_name(self):
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"
    
    @property
    def credits(self):
        return self.__credits

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
    ai_player = AIPlayer()