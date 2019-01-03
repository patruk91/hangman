# hangman
The Hangman Game

**tl;dr**<br />
Program displays dashed word to guess. Next, user enters one letter or whole word.
If user guesses whole word - program displays a win message.
If user guesses a letter - program displays dashed word with uncovered already guessed letters.
If user doesn't guess a letter - program displays the message about wrong answer.
Program works until all letters are uncovered.


**More explanation:**<br />
Create a script that has a list of European capitals, pick one of them randomly and let the user guess it. At the beginning program should represent each letter as a dash ("_") and display them at the screen. Additionally, program should show player's life points (let's say, 5).
Program should ask the user if he/she would like to guess a letter or whole word(s). Next, program waits for the user to enter letter or word. If entered letter doesn't exist in word or entered word is not correct - player will lose a life point. If this action brings player life to zero - the game is over!
If the player survives wrong letter guess - that letter should be added to "not-in-word" list and be displayed at the screen.
If the player guesses final letter or whole word(s) - he/she is the winner! And our world is safe ! :)
You can find detailed explanation of the game at [Wikipedia](https://en.wikipedia.org/wiki/Hangman_%28game%29).
If the basic version works, please implement the following functionalities:
1. Add a question about restarting the program after wins or loses.
2. Add an information about guessing count and guessing time at the end of game (i.e. "You guessed the capital after 12 letters. It took you 45 seconds").
3. There is a file countries_and_capitals.txt containing a list of countries and their capitals (i.e. Poland | Warsaw). Your program should read that file at the beginning and randomly select one country-capital pair. Then, the capital should be the target word(s) to guess. The country should also be remembered - if player will reached his/her life points program should display a hint (i.e. "The capital of Poland").
4. Guessing whole word should be more-risk-more-reward. So, successful guess can save some time, but failing whole word guess should result in losing 2 life points!
5. Add high score - some people take pride in their score. At the end of successful game program should ask user for his/her name and save that information to a file - name| date | guessing_time | guessing_tries | guessed_word (i.e. Marcin | 26.10.2016 14:15 | 45 | Warsaw).
6. Expand high score - program should remember 10 best scores (read from and write to a file) and display them at the end, after success / failure.
7. Add ASCII art! How awesome it will be if after each wrong guess a part of hangman appears? Or a spaceship will be closer to the Earth? Or something different - use your imagination! :)

You can run game in demo mode (you'll get answer(capital)): python3 the_hangman_game.py --demo
