import random as r
computerScore = 0
playerScore = 0
tieScore = 0

choices = ["rock", "paper", "scissors"]

for i in range(10):
    computer = r.choice(choices)
    player = input("Enter your choice: \"rock, paper, or scissors\"").lower()
    if player not in choices:
        print("Invalid Input!")
    if player == computer:
        print("tie")
        tieScore +=1
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
            playerScore +=1
        else:
            print("You lose!")
            computerScore +=1
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            playerScore +=1
        else:
            print("You lose!")
            computerScore +=1
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
            playerScore +=1
        else:
            print("You lose!")
            computerScore +=1

print(f"Player: {playerScore} \nComputer: {computerScore} \nTie Score: {tieScore}")