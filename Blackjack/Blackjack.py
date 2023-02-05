import os
from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player


class Blackjack:
    def __init__(self) -> None:
        self.__intro()

        self.__deck = Deck()
        self.__players = []
        self.__create_players()

        self.__start_round()

    def __create_players(self):
        player = Player()
        player.create()

        self.__players.append(player)

        for _ in range(3):
            ai_player = AIPlayer()
            ai_player.create()
            self.__players.append(ai_player)

    def __start_round(self):
        self.__clear_screen()

        self.__deck.create()

        for player in self.__players:
            player.start_hand(self.__deck)

        for player in self.__players:
            print("-"*50)
            player.draw_card(self.__deck)

        self.__get_winner()

    def __get_winner(self):
        winner_list = [player for player in self.__players if player.hand_value <= 21]

        if winner_list:
            sorted_winner_list = sorted(winner_list, key=lambda player: player.hand_value)
            winner = sorted_winner_list[-1]
            print(f"The winner is {winner}")
        else:
            print("House wins!")
        
        input("Press Enter to continue.")
        self.__ask_new_round()

    def __ask_new_round(self):
        self.__clear_screen()

        player_input = input("Do you want to play again? (y/n)")
        if player_input == "y":
            self.__start_round()
        else:
            print("Maybe next time... Bye!")
            exit()

    def __intro(self):
        self.__clear_screen()
        print("="*50, "BLACKJACK", "="*50)
    
    def __clear_screen(self):
        os.system("cls")


Blackjack()