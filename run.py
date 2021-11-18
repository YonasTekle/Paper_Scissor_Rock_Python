# Importing random library
import random


print("Welcome to Rock Paper Scissors Game")
print()
print("Rules of the  game as follows:\nRock vs paper-> Paper wins\nRock vs scissor-> Rock wins\nPaper vs scissor-> scissor wins \n")

def play_game():

    player_score = 0
    computer_score = 0
   
   
    # Asking for the user input
    while True:
        player = input("rock, paper or scissors? ").lower().strip()
        while player != "rock" and player != "paper" and player != "scissors":
            player = input("Invalid information provided please try again:\n").lower()

        # computer random choice
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
    
        player_wins = 'You win!'
        computer_wins = 'You lost!'

        print()
        # Defining the conditions of Rock,Paper and Scissors
        
        if player == "rock":
            if computer == "rock":
                print("It's A Tie!!!")
                player_score += 1
                computer_score += 1
            elif computer == "paper":
                print(computer_wins)
                computer_score += 1
            elif computer == "scissors":
                print(player_wins)
                player_score += 1
        if player == "paper":
            if computer == "paper":
                print("It's A Tie!!!")
                player_score += 1
                computer_score += 1
            elif computer == "scissors":
                print(computer_wins)
                computer_score += 1
            elif computer == "rock":
                print(player_wins)
                player_score += 1
        if player == "scissors":
            if computer == "scissors":
                print("It's A Tie!!!")
                player_score += 1
                computer_score += 1
            elif computer == "rock":
                print(computer_wins)
                computer_score += 1
            elif computer == "paper":
                print(player_wins)
                player_score += 1
        print() 
        print(f"You played {player}.")
        print()
        print(f"The computer played {computer}.")
        print()
        print(f"Your score: {player_score} - Computer score: {computer_score}")
        print()

        # Asking the user if they want to play again 
        user = input("Do you want to play again? (Y/N)").lower()
        if user == "n":
            print("Thanks for playing!")
            break
        while user != "y" and user != "n":
            user = input("Invalid information provided please try again: (Y/N)").lower()
        if user == 'n':
            print("Thanks for playing!")
            break   
           
        print("\n---------------------------------\n")

play_game()
