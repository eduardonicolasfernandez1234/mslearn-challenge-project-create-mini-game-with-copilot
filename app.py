class RockPaperScissors:
    def __init__(self):
        self.player_count_win = 0
        self.player2_count_win = 0
        self.choices_game = ["r", "p", "s"]

    def play_game(self):
        choices = ["c", "f"]
        print("Welcome to Rock, Paper, Scissors!")
        print("Please choose to play against the computer or a friend.")
        print("Enter 'c' for computer or 'f' for friend.")
        opponent = input("Your choice: ")
        if opponent not in choices:
            print("Invalid choice. Please try again.")
            self.play_game()

        if opponent == "c":
            self.play_computer()
        elif opponent == "f":
            self.play_friend()
        self.play_again()

    def play_computer(self):
        print("You are playing against the computer.")
        print("Enter 'r' for rock, 'p' for paper, or 's' for scissors.")
        player = input("Your choice: ")
        if player not in self.choices_game:
            print("Invalid choice. Please try again.")
            self.play_computer()

        if player == "r":
            print("You chose rock.")
        elif player == "p":
            print("You chose paper.")
        elif player == "s":
            print("You chose scissors.")
        computer = self.computer_choice()
        self.check_winner(player, computer)

    def computer_choice(self):
        import random
        computer = random.choice(self.choices_game)
        if computer == "r":
            print("The computer chose rock.")
        elif computer == "p":
            print("The computer chose paper.")
        elif computer == "s":
            print("The computer chose scissors.")
        return computer

    def check_winner(self, player, player2):
        if player == "r" and player2 == "r":
            print("It's a tie!")
            self.player_count_win += 1
            self.player2_count_win += 1
        elif player == "r" and player2 == "p":
            print("The player2 wins!")
            self.player2_count_win += 1
        elif player == "r" and player2 == "s":
            print("You win!")
            self.player_count_win += 1
        elif player == "p" and player2 == "r":
            print("You win!")
            self.player_count_win += 1
        elif player == "p" and player2 == "p":
            print("It's a tie!")
            self.player_count_win += 1
            self.player2_count_win += 1
        elif player == "p" and player2 == "s":
            print("The player2 wins!")
            self.player2_count_win += 1
        elif player == "s" and player2 == "r":
            print("The player2 wins!")
            self.player2_count_win += 1
        elif player == "s" and player2 == "p":
            print("You win!")
            self.player_count_win += 1
        elif player == "s" and player2 == "s":
            print("It's a tie!")
            self.player_count_win += 1
            self.player2_count_win += 1

    def play_friend(self):
        print("You are playing against a friend.")
        print("Enter 'r' for rock, 'p' for paper, or 's' for scissors.")
        player1 = input("Player 1 choice: ")
        player2 = input("Player 2 choice: ")

        if player1 not in self.choices_game or player2 not in self.choices_game:
            print("Invalid choice. Please try again.")
            self.play_friend()

        if player1 == "r":
            print("Player 1 chose rock.")
        elif player1 == "p":
            print("Player 1 chose paper.")
        elif player1 == "s":
            print("Player 1 chose scissors.")

        if player2 == "r":
            print("Player 2 chose rock.")
        elif player2 == "p":
            print("Player 2 chose paper.")
        elif player2 == "s":
            print("Player 2 chose scissors.")
        self.check_winner(player1, player2)

    def play_again(self):
        print("Would you like to play again?")
        print("Enter 'y' for yes or 'n' for no.")
        again = input("Your choice: ")
        if again == "y":
            self.play_game()
        elif again == "n":
            print("Thanks for playing!")
            if self.player_count_win > self.player2_count_win:
                print("Player 1 wins!")
            elif self.player_count_win < self.player2_count_win:
                print("Player 2 wins!")
            else:
                print("It's a tie!")
            print("Player 1: " + str(self.player_count_win))
            print("Player 2: " + str(self.player2_count_win))
        else:
            print("Invalid choice. Please try again.")
            self.play_again()

# Run the game
game = RockPaperScissors()
game.play_game()
