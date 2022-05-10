import random

def win():
    while True:
        moves=["rock","paper","scissors"]
        computer_choice=random.choice(moves)
        player_choice=None
        while player_choice not in moves:
            player_choice = input('What do you pick? (rock, paper, scissors)').lower()
            if player_choice==computer_choice:
                print("computer:",computer_choice)
                print("player:",player_choice)
                print("draw")
            elif player_choice=="rock" and computer_choice=="paper":
                print("computer:",computer_choice)
                print("player:",player_choice)
                print("you lose")
            elif player_choice=="rock" and computer_choice=="scissors":
                print("computer:",computer_choice)
                print("player:",player_choice)
                print("you win")
            elif player_choice=="scissors" and computer_choice=="rock":
                print("computer:",computer_choice)
                print("player:",player_choice)
                print("you lose")
            elif player_choice=="scissors" and computer_choice=="paper":
                print("computer:",computer_choice)
                print("player:",player_choice)
                print("you win")
            elif player_choice=="paper" and computer_choice=="sciccors":
                print("computer:",computer_choice)
                print("player:",player_choice)
                print("you lose")
            elif player_choice=="paper" and computer_choice=="rock":
                print("computer:",computer_choice)
                print("player:",player_choice)
                print("you win")
        play_again=input("play again?(yes/no):")
        if play_again=="no":
            break
    print("bye")
win()