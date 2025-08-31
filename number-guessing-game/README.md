<h2>Guess The Number</h2>


In this game, the program randomly chooses a number from 1 to 100. The player will attempt to guess that secret number. The player gets feedback if the number the player guesses is higher or lower than the secret number. User can choose between 2 levels (easy and hard). Easy level will give user 10 chances to correctly guess the number and the hard level will give user 5 chances. A good strategy might be to pick a number in the middle and eliminate half of the numbers. 

I started out by defining two constants EASY_LEVEL_TURNS and HARD_LEVEL_TURNS to set the number of turns for different difficulty levels. Then I defined three functions to encapsulate specific functionalities. 'check_answer(guess, answer, turns)': This function checks the user's guess against the answer and returns the number of turns remaining. 'set_difficultly()': This function allows the user to choose the game's difficulty level and returns the number of turns for that level. 'game()': This is the main game function that contains the core game logic. 

Created an engaging user interface by printing messages and getting user input with the 'print()' and 'input()' functinons. Used the 'randint()' function to generate a random number within a specified range (1 and 100) and stored it in the 'answer' variable. Conditional Statements were implemented to handle different scenarios to check the user's chosen difficulty level and determine the number of turns accordingly. The game was created in a loop such that it allows the user to keep guessing until they either guess the correct number, or run out of turns, or decides to exit the game. 

<br/>

<img src="https://i.imgur.com/2pVoWp4.png" alt="image"/>
