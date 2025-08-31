# Step 5

import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

display = []
wrong_letters = []

print(logo)

# Testing code
# print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if letter already guessed
    if guess in display or guess in wrong_letters:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word and guess not in wrong_letters:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        wrong_letters.append(guess)
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    if not end_of_game:
        print(stages[lives])
