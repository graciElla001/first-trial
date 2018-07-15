#guess_my_number game 2

print("\tWelcome to 'Guess My Number'!")
print("\nThe compuer is thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

import random
#The computer guesses a random number between 1 and 100
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
count = 0

while guess != the_number:
    if count >= 10:
        print("why are you so slow at guessing??")
    else:
        print("you ae such a fast guesser.")

guess = int(input("Take another guess: "))
tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

guess = int(input("Take another guess: "))
tries += 1

input("\n\nPress the enter key to exit.")



