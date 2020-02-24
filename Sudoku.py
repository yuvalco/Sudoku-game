
def solve_board(board):
    """
    backtracking recursion that solve a sudoku board
    :param board:
    :return: if board is solvable returns true, otherwise return false.
    """
    empty_space = find_empty_space(board)

    if not empty_space:
        return True

    i, j = empty_space

    # attempts each number from 1 to 9 on empty space.
    for value in range(1, 10):
        if valid(board, empty_space, value):
            board[i][j] = value

            if solve_board(board):
                return True

            board[i][j] = 0

    return False


def valid(board, location, value):
    """
    checks if a value fit the location.
    the rules are, no 2 numbers in the same row, col , or 3*3 block

    :param board: the board we are checking
    :param location: gets a location (x,y)on the board of an empty space
    :param value: the number we would like to check if fits the location"""

    row = location[0]
    col = location[1]

    # checks for row
    for i in range(9):
        if i != row and board[i][col] == value:
            return False
    # checks for col
    for j in range(9):
        if j != col and board[row][j] == value:
            return False

    # block-checks row
    # if the row of the block is the same as the row of the value, than no need to
    # check since we did it in the previous loops.
    start_row = int(row / 3) * 3
    for start_row in range(start_row, start_row + 3):
        if row != start_row and board[start_row][col] == value:
            return False

    # block-checks col
    start_col = int(col / 3) * 3
    for start_col in range(start_col, start_col + 3):
        if col != start_col and board[row][start_col] == value:
            return False

    return True


# prints the board to console.
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# find places to fill in the Soduku board.
def find_empty_space(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return False
