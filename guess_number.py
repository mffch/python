'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (_Hint: remember to use the user input lessons from the very first exercise

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random
x=random.randint(1,9)

count=0
while user != "exit" and user != x:
    user=input("Guess the number:")
    user=int(user)
    count+=1
    
    if user == "exit":
        break
    if user == x:
        print("You guessed!")

    else:
        if user < x:
            print("Your number is too low!")
        else:
            print("Your number is too high!")
 

print("The user tried" + str(count))
   
    