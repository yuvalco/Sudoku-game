# Sudoku-game
A Sudoku game that checks if you are right by using backtracking algorithm to solve the board.

### GUI.py
Contains everything related to the ui.  
Has class called grid that contains an instance of each cube on the board.  
Our main() is found here.
### Cube.py
Contains one class Called Cube.  
Each "cube" or cell on the board has it's own value, bounds, and other properties.
### Sudoku.py
This files has no classed but only functions.
#### solve_board(board)
Solves a given board by backtracking algorithm that checks each and every poassible outcome untill it's finds valid one.
#### valid(board, location, value)
Checks whether a given value in a given location is valid for a spesfic board.
#### find_empty_space(board)
Searches for empty location on the board.

# Images
### Board
![image1](https://github.com/yuvalco/Sudoku-game/blob/master/1.png)

### Board with selected cube and some values filled in.
![image2](https://github.com/yuvalco/Sudoku-game/blob/master/2.png)
