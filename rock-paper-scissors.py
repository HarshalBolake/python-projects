import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    player_choice = input("Choose rock, paper or scissors: ").lower()

    if player_choice not in choices:
        print("Please choose rock, paper or scissors.")
    elif player_choice == computer_choice:
        print("Its a tie!")
    elif(
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

    print("Computer choice:", computer_choice)


play_game()

