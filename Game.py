from time import sleep
from Die import Die
from Player import Player
import os


class Game:
    """
    This class represents the dice game, it has two attributes
    player, and computer which are instances of a player.
    """
    def __init__(self, player: Player, computer: Player):
        self._player = player
        self._computer = computer

    @property
    def player(self):
        return self._player

    @property
    def computer(self):
        return self._computer

    def game_over(self) -> bool:
        if self.player.counter == 0:
            print(f"\ncongratulation {self.player.name} you won the game!!!")
            return True
        elif self.computer.counter == 0:
            print(f"\ncongratulation {self.computer.name} you won the game!!!")
            return True
        else:
            return False

    @staticmethod
    def welcome_message() -> None:
        print("---------------------------------------------------")
        print(f'--------------- Welcome to Dice Game--------------')
        print("---------------------------------------------------")

    @staticmethod
    def end_message() -> None:
        print("\n------------ Game Over!!! -----------------")

    def announce_player(self) -> None:
        print(f"\nThis Game is between {self.player.name} and {self.computer.name}")

    def display_counter(self):
        print(f"{self.player.name}'s counter: {self.player.counter}")
        print(f"{self.computer.name}'s counter: {self.computer.counter}")

    def start_a_round(self):
        print('\n------ New Round --------')
        player_number = self.player.roll_the_die()
        computer_number = self.computer.roll_the_die()
        if player_number > computer_number:
            print(f"{self.player.name} won this round!!!")
            self.player.decrement_counter()
            self.computer.increment_counter()
            Game.display_counter(self)
        elif computer_number > player_number:
            print(f"{self.computer.name} won this round!!!")
            self.computer.decrement_counter()
            self.player.increment_counter()
            Game.display_counter(self)
        else:
            print("There is a tie")
            Game.display_counter(self)


def main():
    die1 = Die()
    die2 = Die()

    player = Player(die1, "Andrew", is_human=True)
    computer_ = Player(die2, "computer_", is_human=False)

    game = Game(player, computer_)
    game.welcome_message()
    game.announce_player()
    sleep(2)
    os.system('clear')

    # game.start_the_game()
    while True:
        input("Press Enter key to roll a dice: ")
        os.system("clear")
        game.start_a_round()
        if game.game_over():
            game.end_message()
            break


if __name__ == "__main__":
    main()