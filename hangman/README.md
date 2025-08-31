<h2>Hangman Game</h2>

Hangman is a word-guessing game that is commonly played with a pencil and paper. It's usually played by two or more people, with one person thinking up a word and drawing a series of blank spots, one for each letter in the word. The other players then take turns guessing letters in an attempt to decipher the secret word.

The game is called "Hangman" because of the visual feature that it frequently includes. A part of a hangman figure (a stick figure) gets drawn for each wrong guess. Typically, the game begins with an empty gallows or a hangman figurine. Each wrong estimate results in the addition of a new body part (head, body, arms, legs) to the hangman figure. The players' goal is to guess the word.

In this program, a secret word is randomly chosen from a list. An for-loop was used to iterate the length of characters in the secret word and appended "_" underscores to a display list. When user guesses a letter, the program checks if letter is in secret word and in the wrong_letter list. When user guesses wrong letter, it subtracts 1 life and appends the wrong letter into a wrong_letter list. When user guesses the correct letter, program replaces the index of the display_list with the index from the secret word. Since the program keeps tracked of wrong letters, user will not be deducted additional lives for guessing the same wrong letter more than once.  


<img src="https://i.imgur.com/JuZEbSx.png" alt="image"/>
