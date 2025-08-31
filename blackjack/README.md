<h2>Blackjack</h2>

Blackjack, also known as 21, is a popular card game played in casinos around the world. It is a comparing card game between one or more players and a dealer, with each player competing against the dealer rather than against each other.

The primary objective of blackjack is to beat the dealer by having a hand value that is closer to 21 points without exceeding it. Player can ask for more cards as long as player does not go over 21. Dealer must get cards if hand is below 17. 

I created a deal_card function that returns a random card from a predefined list of card values (including face cards and aces). Aces will initially have card value of 11. Another function calculate_score is used to calculate the total score based on a list of cards considering the special case of aces being worht 11 or 1. If sum of card value equals 21 and length of cards equals 2 that would be considered as blackjack. If 11 was in cards and the sum of cards is greater than 21, value with value 11 would be replaced with 1. Another function was used with if, elif, else statments to compare user score and computer score to determine which player won by opponent going over 21, or blackjack, or having a draw. 

The 'play_game()' function represents a single game of Blackjack. It initializes the user's and computer's card lists and deals two cards to each player. It allows user to choose to get more cards or pass. It also manages the computers moves based on a simple rule (draw until a score of 17 or higher is reached). 

The main game loop continously asks the player if they want to play. If the player answers 'y', a game is played using the 'play_game()' function. The loop continues until the player decides to stop playing by entering 'n'. 

During each game the user is dealt two cards, and the game proceeds by asking the user if they want to draw additional cards or pass. The computer follows its predefined rule for drawing cards. Once both the user and computer have completed their turns, the outcome is determined using the 'compare()' function, and the results are displayed. 

<br/>

<img src="https://i.imgur.com/fhhWtZy.png" alt="image"/>
