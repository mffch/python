'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

'''

play1=(input("Enter play1: "))
play2=(input("Enter play2: "))

while True:
    if play1==play2:
        print("It is a tide")
    elif play1=="rock" and play2=="scissors":
        print("Player 1 wins cause rock beats scissors")
    elif play2=="rock" and play1=="scissors":
        print("Player 2 wins cause rock beats scissors")
    elif play1=="rock" and play2=="paper":
        print("Player 2 wins cause Paper wins to rock")
    elif play2=="rock" and play1=="paper":
        print("Player 1 wins cause Paper wins to scissors")
    elif play1=="paper" and play2=="scissors":
        print("Player 2 wins cause Scissors wins to scissors")
    elif play2=="paper" and play1=="scissors":
        print("Player 1 wins cause Scissors wins to scissors")

    break    