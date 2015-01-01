Mastermind
==========

Playable Mastermind in Python, with an AI that hints the player on the best possible guess.

This is an implementation of the well-known board game Mastermind.
The goal is to find a randomly generated number, composed of 4 [1-6]-digits (1296 possibilities), within 6 tries.
After each try, the computer tells the player the number of correct and well-placed digits (B for "Black"),
and the number of correct but mis-placed digits (W for "White").

At every moment, the player can ask for the "state" of the game by writing "etat" : this gives all the possible
numbers, in regards with the computer's answers to the player's guesses.
He can also ask for help by typing "conseil". An AI will then tell him the best possible guess in regards with the
current state of the game, and the algorithm implemented.

This is an implementation of Donald Knuth's mini-max algorithm for Mastermind. The computer's guess is the guess that
would remove the most possibilities in the worst case. Note that it is possible - and it happens regularely - that the 
best guess is a number that has already been invalidated (that is not in the current state of the game).
If we use as first guess '1122' and then use the algorithm for each try, it is guaranteed that we will win.
