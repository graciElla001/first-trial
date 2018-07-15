#guess_my_number game

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

import random

#The computer guesses a random number between 1 and 100
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

if tries > 4:
    print("You are very poor at guessing o...")
else:
    print("WAWU!!! oya clap for yourself,you are a good guesser(smiles).")

input("\n\nPress the enter key to exit.")

