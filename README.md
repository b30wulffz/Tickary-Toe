# Tickary-Toe
A computer vs human tic tac toe based on Ursina Engine

## Game Play: 
The game consists of 2 modes: 

* Classic 3v3 - It is based on basic minimax.
* Advanced - Using this mode, one can change board size, cutoff size, algorithm and depth.

In the home page of the game, the user can choose who is going to start first: computer or himself.

```
While playing, one can press F11 key to toggle fullscreen.  
```

Youtube Link: https://youtu.be/s3FNXD9-q6w

## Instructions: 
* For basic minimax and alpha-beta pruning, keep the board size up to 3.
* The cutoff is the number of naughts or crosses required to win a game.
* If the given board size is smaller than the cutoff, then the cutoff will be changed to the board size.
* For depth-based algorithms, keeping depth up to 3 can make it work smoothly.
* Experimental algorithms are optimised to work better. But still, there are chances that the algorithm ends up failing.
* The rules mentioned above, if not followed, might crash the game.

## How to run?
You need to install Ursina Engine, by following these steps:
* Install Python 3.6 or newer
* Make sure you have git installed.
* Open cmd/terminal and type:
  `pip install git+https://github.com/pokepetter/ursina.git`
* Navigate to TickaryToe folder by `cd TickaryToe`
* Run `python main.py`

The game will be launched.
