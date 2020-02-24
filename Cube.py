lastCubeSelected = None


class Cube:
    """
    Class that represent a cube on the board.
    :param value the cube's value on the board.
    :type value int
    :param row the cube row number
    :type row int
    :param col the cube col number
    :type col int
    :param width the width of the widget or window we are drawing on
    :type width int
    :param height the height  of the widget or window we are drawing on
    :type height int
    :param canvas the canvas we are drawing on
    :type canvas object tk.Canvas
    """

    def __init__(self, value, row, col, width, height, canvas):
        self.col = col
        self.row = row
        self._temp = 0
        self.height = height
        self.width = width
        self._value = value
        self.selected = False
        self.rect = None
        self.canvas = canvas
        self.cube_text = None

        # calculates the bounds of the cube
        gap = self.width / 9
        self.x = gap * col
        self.y = gap * row
        self.end_x = self.x + gap
        self.end_y = self.y + gap

        self.position_num = (self.x + self.end_x) / 2, (self.y + self.end_y) / 2

        # if cube in not empty at the beginning of the game than draw it's number.
        if value is not 0:
            self.canvas.create_text(self.position_num, fill="black", font="Times 20", text=value)

        """:param selected indicates whether the cube is selected or not
          :param """

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        """
        sets a temp value until the user decides to click enter
        :param value: the temp value for the cube
        :return:
        """
        self.delete_text()
        self._temp = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.cube_text = self.canvas.create_text((self.x + self.end_x) / 2, (self.y + self.end_y) / 2, fill="black",
                                                 font="Times 20",
                                                 text=value)
        self._value = value

    def select(self, canvas):
        """
        highlighting the selected cube with a red rectangle and sets the cube as selected.
        if already selected than the function deselect the cube.
        :param canvas: our main canvas we are drawing on.
        :returns whether the cube was selected(true) or deselected(false), the row, and col of the cube.
        """
        if self.selected:
            self.selected = False
            canvas.delete(self.rect)
        else:
            canvas.delete(globals()['lastCubeSelected'])
            globals()['lastCubeSelected'] = self.rect = canvas.create_rectangle(self.x, self.y, self.end_x,
                                                                                self.end_y,
                                                                                width=3, outline="red")
            self.selected = True

        return {"is_selected": self.selected, "row": self.row, "col": self.col}

    def draw_temp_num(self, value):
        """
        draws a temp value on the cube.
        :param value: the value to draw
        :type value int
        """
        self.cube_text = self.canvas.create_text((self.x + self.end_x) / 2, (self.y + self.end_y) / 2, fill="grey",
                                                 font="Times 20",
                                                 text=value)

    def delete_text(self):
        """
        deletes the text that is writen on the cube.
        """
        self.canvas.delete(self.cube_text)
