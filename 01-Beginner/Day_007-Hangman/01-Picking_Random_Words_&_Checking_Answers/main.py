# Step 1
# TO DO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TO DO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TO DO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

word_list = ["aardvark", "baboon", "camel"]
# To do 1
import random

chosen_word = random.choice(word_list)
# print(chosen_word)

# To do 2
guess = input("Guess a letter: ").lower()
# print(guess)

# to do 3
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")