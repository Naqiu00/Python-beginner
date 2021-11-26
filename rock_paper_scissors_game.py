# rock paper scissors

import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock , paper or scissors? :: ').lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("TIE!!")
    elif player == 'rock':
        if computer == 'paper':
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!!")
        if computer == 'scissors':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!!")
    elif player == 'scissors':
        if computer == 'rock':
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!!")
        if computer == 'paper':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!!")
    elif player == 'paper':
        if computer == 'scissors':
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!!")
        if computer == 'rock':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!!")
    
    play_again = input("Play again? (YES/NO) :  ").lower()

    if play_again != "yes":
        break

print("BYE!!")