import tkinter
from Cube import Cube
from Sudoku import solve_board, valid

# dict that indicates whether a cube is selected or not and it's row and col.
selected = None
# key codes for keys
code = {"DELETE": 46, "ENTER": 13, "1": 46, "NUM_PAD_1": 97, "9": 57, "NUM_PAD_9": 105}


class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height, canvas):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[i][j], i, j, width, height, canvas) for j in range(cols)] for i in range(rows)]
        self.canvas = canvas
        self.selected_cube_data = {"is_selected": False, "row": 0, "col": 0}
        self.moded_board = [[self.board[i][j] for j in range(self.cols)] for i in range(self.rows)]

        # draws the grid of the board
        gap = self.width / 9

        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                width = 3
            else:
                width = 1

            canvas.create_line(gap * i, 0, gap * i, self.height, width=width, fill="black")
            canvas.create_line(0, gap * i, self.width, gap * i, width=width, fill="black")

    def select(self, position):
        gap = self.width / 9
        i, j = int(position.y / gap) % 9, int(position.x / gap) % 9
        self.selected_cube_data = self.cubes[i][j].select(self.canvas)
        globals()['selected'] = self.selected_cube_data

    def key_pressed(self, key):
        """
        called when an event of key pressed is fired
        :param key: the key that was pressed
        """

        # checks if some cube is selected
        if selected["is_selected"]:
            row = self.selected_cube_data["row"]
            col = self.selected_cube_data["col"]

            # checks if the pressed key is between 1-9 keyCodes
            if code['1'] <= key.keycode <= code['9'] or code['NUM_PAD_1'] <= key.keycode <= code['NUM_PAD_9']:
                self.cubes[row][col].temp = int(key.char)
                self.cubes[row][col].draw_temp_num(key.char)

            # the user pressed delete
            if key.keycode == code['DELETE']:
                self.cubes[row][col].temp = 0
                self.cubes[row][col].delete_text()

            # the user pressed enter
            if key.keycode == code['ENTER']:
                if selected['is_selected']:
                    row, col = selected["row"], selected["col"]

                    if self.cubes[row][col].temp != 0:
                        self.moded_board[row][col] = self.cubes[row][col].temp

                        # prints to console if valid or not, used for debug.
                        print(valid(self.moded_board, (row, col), self.cubes[row][col].temp))

                        # if ain't valid or ain't solvable than will erase the number on the selected cube after user
                        # pressed enter.
                        if not (valid(self.moded_board, (row, col), self.cubes[row][col].temp) and solve_board(
                                self.moded_board)):
                            print("not valid " + str(self.cubes[row][col].temp) + str((row, col)))
                            self.moded_board[row][col] = 0
                            self.cubes[row][col].temp = 0
                            self.cubes[row][col].delete_text()
                        else:
                            self.cubes[row][col].delete_text()
                            self.cubes[row][col].value = self.cubes[row][col].temp


def main():
    window_width = 540
    window_height = 600
    bottom_margin = 60
    gird_size = 9

    size = str(window_width) + "x" + str(window_height)

    # initiate window and set properties.
    window = tkinter.Tk()
    window.geometry(size)
    # None resizable
    window.resizable(0, 0)

    canvas = tkinter.Canvas(window, height=window_height - bottom_margin, width=window_width)
    board = Grid(gird_size, gird_size, window_width, window_height, canvas)
    # subscribing to events
    canvas.bind("<Button-1>", board.select)
    window.bind("<Key>", board.key_pressed)
    canvas.pack()
    window.mainloop()


main()
