<h2>Caesar Cipher</h2>

A Caesar cipher, also known as a Caesar shift or a shift cipher, is one of the simplest and oldest methods of encryption. It is a type of substitution cipher in which each letter in the plaintext is shifted a fixed number of positions down or up the alphabet. This fixed number is often referred to as the "key" or "shift value."

The user determines how many positions each letter in the plaintext will be shifted in the alphabet. The program will output the corresponding encrypted message. To decrypt, user will need to enter the encrypted message along with the shift number.

To achieve this, I created a function that takes input from user the: start_text, shift_amount, and cipher direction (encode/decode). When encoding text, used a for-loop to iterate through each character in the start_text and if that character was in my alphabet list, program would save into a position variable of the index location the character in the alphabet list. I created a new_position variable that added the shift_amount to the index position variable. I created an empty list named end_text which concatenated the index of the new_position in the alphabet list within the loop. To decode, I used an if-statement before the for-loop, that multiplies the shift_amount by -1 to reverse direction. In case user enters a shift amount by a number greater than 26, when I assigned the shift value from user input, I used the modulo 26 operation to the shift variable. This was done to ensure that the shift value stays within the range of 0 to 25, which corresponds to the 26 letters in the English alphabet. This ensures that the shift value is valid for a Caesar cipher. 

</br>

<img src="https://i.imgur.com/RuPqi0x.png" alt="image"/>
