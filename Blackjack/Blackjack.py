import os, time
from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player


class Blackjack:
    def __init__(self) -> None:
        self.__intro()

        self.__deck = Deck()
        self.__players = []

        # create player and store it as an attribute of Blackjack
        self.__player = Player()
        self.__player.create()
        self.__players.append(self.__player)

        self.__create_players()
        self.__bet = 0
        self.__min_bet = 10

        self.__start_round()

    def __create_players(self):
        for _ in range(3):
            ai_player = AIPlayer()
            ai_player.create()
            self.__players.append(ai_player)

    def __start_round(self):
        self.__clear_screen()
        self.__deck.create()

        players_cant_play = [player for player in self.__players if not player.has_credits(self.__min_bet)]

        # remove players who couldn't give bet
        for player in players_cant_play:
            print(f"{player} losts his/her all credits :(")
            self.__players.remove(player)

        # start player hands and get credits from players
        for player in self.__players:
            player.start_hand(self.__deck)
            self.__bet += player.give_bet(self.__min_bet)

        # start round for players
        for player in self.__players:
            print("-"*50)
            player.draw_card(self.__deck)

        time.sleep(1)
        self.__get_winner()

    def __get_winner(self):
        self.__clear_screen()
        winner_list = [player for player in self.__players if player.hand_value <= 21]

        if winner_list:
            sorted_winner_list = sorted(winner_list, key=lambda player: player.hand_value)
            winner = sorted_winner_list[-1]
            print(f"The winner is {winner}. Hand value: {winner.hand_value}")
            print(f"{winner} wins {self.__bet} credits")
            winner.reward(self.__bet)

            print("-"*50)
            for player in sorted_winner_list:
                player.reveal_hand()
        else:
            print("House wins!")
        
        input("Press Enter to continue.")
        self.__ask_new_round()

    def __ask_new_round(self):
        self.__clear_screen()

        if self.__player.has_credits(self.__min_bet):
            player_input = input("Do you want to play again? (y/n)")
            if player_input == "y":
                self.__start_round()
            else:
                print("Maybe next time... Bye!")
                exit()
        else:
            print("You lost all your credits... Maybe next time :(")
            exit()

    def __intro(self):
        self.__clear_screen()
        print("="*50, "BLACKJACK", "="*50)
    
    def __clear_screen(self):
        os.system("cls")


Blackjack()