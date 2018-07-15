# Loopy String
# Demonstrates the for loop with a string
word = input("Enter a word: ")
print("\nHere's each letter in your word:")
for letter in word:
    print(letter)
input("\n\nPress the enter key to continue.")

# Counter
# Demonstrates the range() function

print("Counting:")
for i in range(10):
    print(i, end=" ")
print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end=" ")
print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")
input("\n\nPress the enter key to continue.")

# Message Analyzer
# Demonstrates the len() function and the in operator

message = input("Enter a message: ")
print("\nThe length of your message is:", len(message))
print("\nThe most common letter in the English language, 'e',")
if "e" in message:
    print("is in your message.")
else:
    print("is not in your message.")
input("\n\nPress the enter key to continue.")

# Random Access
# Demonstrates string indexing

import random

word = "divine"
print("The word is: ", word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])
input("\n\nPress the enter key to continue.")

# No consonants
# Demonstrates creating new strings with a for loop

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created:", new_message)
        print("\nYour message without consonants is:", new_message)
input("\n\nPress the enter key to exit.")
