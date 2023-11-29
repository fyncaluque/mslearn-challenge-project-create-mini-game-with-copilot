# Import module
import random

# Define variable
# List of option
option = ["rock", "paper", "scissors"];
points_player = 0
points_computer = 0
rounds = 0

# Define function
# Function to print the result
def print_result(player, computer):
    global points_player, points_computer, rounds 
    rounds += 1
    print("Player: " + player)
    print("Computer: " + computer)
    if player == computer:
        points_player += 1
        points_computer += 1
        print("Draw")
    elif player == "rock":
        if computer == "paper":
            points_computer += 1
            print("Computer win")
        else:
            points_player += 1
            print("Player win")
    elif player == "paper":
        if computer == "scissors":
            points_computer += 1
            print("Computer win")
        else:
            points_player += 1
            print("player win")
    elif player == "scissors":
        if computer == "rock":
            points_computer += 1
            print("Computer win")
        else:
            points_player += 1
            print("Player win")
    
# Function to print the score
def print_score():
    global points_player, points_computer, rounds
    print("====================================")
    print("Rounds: " + str(rounds))
    print("Player points: " + str(points_player))
    print("Computer points: " + str(points_computer))
    print("====================================")

# Function to play the game
def play_game():
    # Define variable
    player = input("Rock, Paper, Scissors? ")
    player = player.lower()
    #Verification input option valid
    if player not in option:
        print("Wrong input")
        play_game()
    else:
        computer = random.choice(option)
        print_result(player, computer)

# Function to play again
def play_again():
    # Define variable
    again = input("Play again? (y/n) ")
    if again == "y":
        play_game()
        play_again()
    elif again == "n":
        print_score()
        print("Thank you for playing")
    else:
        print("Wrong input")
        play_again()

# Function to start the game
def start_game():
    play_game()
    play_again()

# Start the game
start_game()


