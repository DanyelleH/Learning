# Write a program that prompts the user for an integer that the player will try 
# to guess. If the player's guess is higher than the target integer,
#  the program should display "too high". If the user's guess is lower 
# than the target integer, the program should display "too low". The program 
# should use a loop that repeats until the user correctly guesses the integer. 
# Then the program should print how many guesses it took.  When you run your
#  program it should match the following format:

# Enter the integer for the player to guess.
# -12
import random

won = False


targetNumber= random.randint(1,11)
counter = 0
while won == False:
    players_guess = int(input("Enter your guess"))
    counter+=1
    if players_guess == targetNumber:
        print(f"You got it in {counter} tries")
        won = True
    elif players_guess < targetNumber:
        print( "Too low, try again")
    else:
        print("Too high, try again")
            