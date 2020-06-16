# py_blackjack
Blackjack game written in Python using OOP

This project is comprised of three Python files:
  1. bj_classes.py
      This file contains the defining of <Card>, <Deck>, and <Player> classes through attributes and methods used by instances of these classes.
  2. players.py
      This file contains a function through which is created a list with four players whose attributes are extracted from 'ParticipantsList.txt'
  3. bj_game.py
      This file contains the program for the Blackjack game utilising instances and methods of the classes defined in the <bj_classes.py> file,
the function defined in the <players.py> file, and other functions necessary for unrolling the game of Blackjack.

The game is defined inside the <blackjac()> function and placed within a <while> loop: "while chips > 0:". Therefore, a round of the game can be
played while the human player has at least 1 chip. The game ends when the human player remains without chips to bet. In that moment, the 
<new_game()> function is called, through which the player is asked if s/he want's to play again. In case of an afirmative answer, a new list
players list is generated (for reseting the number of chips) and the human player has randomly assigned a player from the list of four and 
reenters the loop defined inside the <blackjack()> function.
