import os

class Blackjack:
    def __init__(self) -> None:
        self.__intro()

    def __intro(self):
        self.__clear_screen()
        print("="*50, "BLACKJACK", "="*50)
    
    def __clear_screen(self):
        os.system("cls")


Blackjack()