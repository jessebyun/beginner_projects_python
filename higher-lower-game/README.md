<h2>Higher Lower Game</h2>

The "Higher or Lower" game, also known as "Higher Lower," is a simple and entertaining card game where players attempt to guess whether the next card in a sequence will be higher or lower in rank than the previous one. Using the same concept, in this game the player will be given 2 accounts from a instagram account list and the player will try to guess who has more followers. If user chooses correctly, a score will be tracked. The next round, the user will have to guess again who has more followers and the new account will be compared with the account from the previous round. 

In this program I defined two functions: 'format_data(account)' this function takes account the dictionary and formats its data into a printable format; and 'check_answer(guess, a_followers, b_followers)' this function checks whether the user's guess is correct by comparing the follower counts of two accounts. First I initialized the score and game continuation variables. Inside the game loop, I selected two random accuonts from the 'data' and displayed their information to the user. The user is prompted to make a guess (either A or B) about which account has more followers. The code checcks if the user's guess is correct by comparing the follower counts of the two accounts using the 'check)answer()' function. If user is correct, their score is increased by 1, and the game continues with a new pari of accounts. The user is provided with their current score. If user is incorrect, the game ends, and the final score is displayed. Game continues until the user decides to stop playing. The code also clears the screen between rounds, ensuring a clean display. 

<br/>

<img src="https://i.imgur.com/xRFp9RS.png" alt="image"/>
