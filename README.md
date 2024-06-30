# Introduction
This is a simple Sudoku solver application developed as a personal project. The application is written in Python and uses the backtracking recursion algorithm to solve Sudoku puzzles. It provides a user-friendly graphical user interface (GUI) for users to input and solve Sudoku puzzles.

# Features
Sudoku Solver: The application can solve standard 9x9 Sudoku puzzles using the backtracking algorithm, ensuring a valid and complete solution.

Interactive GUI: Users can interact with the Sudoku solver through a graphical user interface, making it easy and intuitive to input and solve puzzles.

## Demonstration of backtracking
![gif](https://github.com/yuvalco/Sudoku-game/blob/master/sudoku.gif)

### GUI.py
Contains everything related to the UI.
Includes a class called Grid that contains an instance of each cube on the board.
The main() function is found here.
### Cube.py
Contains one class Called Cube.  
Each "cube" or cell on the board has it's own value, bounds, and other properties.
### Sudoku.py
This file has no classes, only functions.
#### solve_board(board)
Solves a given board using the backtracking algorithm that checks every possible outcome until it finds a valid one.
#### valid(board, location, value)
Checks whether a given value in a specific location is valid for a given board.
#### find_empty_space(board)
Searches for empty location on the board.


# Images
### Board
![image1](https://github.com/yuvalco/Sudoku-game/blob/master/1.png)

### Board with selected cube and some values filled in.
![image2](https://github.com/yuvalco/Sudoku-game/blob/master/2.png)
