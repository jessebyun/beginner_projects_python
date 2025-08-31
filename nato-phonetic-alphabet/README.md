<h2>NATO Phonetic Alphabet</h2>

This program will spell out a word that the user inputs into the NATO alphabet.

Utilizing list and dictionary comprehension can greatly reduce the lines of code that a developer needs to write. This program will utilize list and dictionary comprension to complete this task. Using the pandas library with the panda.iterrows() method, a CSV file will be read containing the letters of the alphabet with a corresponding NATO code. Although the pandas library has the panda.to_dict() method, this will not be in a useable format, therefore, I will utilize dictionary comprehension to get the data in a format that I can use "{"A": "Alfa", "B": "Bravo"}". Once I have the data in this format, I will then use list comprehension to iterate through the letters of the word the user inputs and then output an list with the NATO codes. 


<img src="https://i.imgur.com/Z6KnIIW.png" alt="image"/>
