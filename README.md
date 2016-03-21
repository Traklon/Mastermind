Mastermind
==========

Playable Mastermind in Python, with an AI that hints the player on the best possible guess.

This is an implementation of the well-known board game Mastermind.
The goal is to find a randomly generated number, composed of 4 [1-6]-digits (1296 possibilities), within 6 tries.
After each try, the computer tells the player the number of correct well-placed digits (blacks) and the number of correct
but mis-placed digits (whites).

This implementation is more than just a playable Mastermind: at every moment, the player can ask for the "state"
of the game, giving all the possible codes in regards with the computer's answers to the player's guesses.
He can also ask for help: an AI will then tell him the best possible guess in regards with the
current state of the game, and the algorithm implemented.

This is an implementation of Donald Knuth's mini-max algorithm for Mastermind. The computer's guess is the guess that
would remove the most possibilities in the worst case. Note that it is possible - and it happens regularely - that the 
best guess is a number that has already been invalidated (that is not in the current state of the game).
Using the algorithm at every try guarantees a win.

How to play
-----------

There are 2 modes. One allows you to play agains the computer ("Normal mode"), and one allows you to only use the algorithm as a helper for a "real life" game ("Helper mode").

In both modes, you can at any time ask for the best possible guess typing:

    help

And for all the remaining possible codes typing

    state

Normal mode
----------

To start:

    python mastermind.py

The computer generates randomly a value that you have to guess. You can input your guesses directly.

Example:

    1234

Helper mode
----------

To start:

    python mastermind.py help

You have to input your guesses using this syntax: 

    <guess> <blacks> <whites>

For example, if you tried '1234' and got 2 well placed and 1 misplaced, simply type:

    1234 2 1

You can indicate that you won typing:

    win
