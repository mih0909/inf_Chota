from tkinter import *
from random import randint


class Game:

    WIDTH = 7
    HEIGHT = 7
    MINES = 10
    CELL_WIDTH = 38
    CELL_HEIGHT = 41
    def __init__(self):
        root = Tk()

        root.geometry(f'{self.WIDTH * self.CELL_WIDTH}x{self.HEIGHT * self.CELL_HEIGHT}')
        root.maxsize(self.WIDTH * self.CELL_WIDTH, self.HEIGHT * self.CELL_HEIGHT)
        root.minsize(self.WIDTH * self.CELL_WIDTH, self.HEIGHT * self.CELL_HEIGHT)

        field = set_field(self.WIDTH, self.HEIGHT, root)
        set_mines(self.MINES, field)
        set_numbers(field)
        # print(field)
        print(field[0][0].round)
        root.mainloop()

    def terminate(self):
        del self
class Mine:

    def __init__(self, _master, _x, _y, ):
        self.btn = Button(master=_master, width=4, height=2, bg='gray',)
        self.btn.grid(row=_y, column=_x)
        self.is_bomb = False
        self.r_cnt = 0
        self.btn.config(command=self.on_clic)
        self.round = [None] * 8


    def set_mine(self):
        self.is_bomb = True
        self.btn.config(bg="red")

    def check_around(self, lst: list):
        self.round = lst[:]
        for i in self.round:
            if i and not i.is_bomb:
                i.btn.config(bg='green')

    def on_clic(self):
        if self.is_bomb:
            del game
        self.btn.config(text=f'{self.r_cnt}')
        # self.btn.destroy()
        # print(1)
        pass

    def detonate(self):
        pass

    def open(self):
        pass

def set_field(width, height, master):
    mines = [[Mine(_master=master, _x=x, _y=y) for x in range(width)] for y in range(height)]
    return mines


def set_mines(m_cnt: int, lst: list):
    for i in range(m_cnt):
        a = lst[randint(0, len(lst)-1)][randint(0, len(lst[0])-1)]
        a.set_mine()


def set_numbers(field):
    y_e = len(field)
    x_e = len(field[0])
    for y in range(y_e):
        for x in range(x_e):
            if field[y][x].is_bomb:
                print(y, x, end=' бомба\n')
                env = [
                    [None, field[(y - 1) % y_e][(x - 1) % x_e]][0 <= y - 1 <= y_e and 0 <= x - 1 <= x_e],
                    [None, field[(y - 1) % y_e][(x + 0) % x_e]][0 <= y - 1 <= y_e and 0 <= x + 0 <= x_e],
                    [None, field[(y - 1) % y_e][(x + 0) % x_e]][0 <= y - 1 <= y_e and 0 <= x + 1 <= x_e],
                    [None, field[(y + 0) % y_e][(x - 1) % x_e]][0 <= y + 0 <= y_e and 0 <= x - 1 <= x_e],
                    [None, field[(y + 0) % y_e][(x + 1) % x_e]][0 <= y + 0 <= y_e and 0 <= x + 1 <= x_e],
                    [None, field[(y + 1) % y_e][(x - 1) % x_e]][0 <= y + 1 <= y_e and 0 <= x - 1 <= x_e],
                    [None, field[(y + 1) % y_e][(x + 0) % x_e]][0 <= y + 1 <= y_e and 0 <= x + 0 <= x_e],
                    [None, field[(y + 1) % y_e][(x + 1) % x_e]][0 <= y + 1 <= y_e and 0 <= x + 1 <= x_e],
                ]
                field[x][y].check_around(env)


if __name__ == '__main__':

    game = Game()

    # WIDTH = 7
    # HEIGHT = 7
    # MINES = 10
    # CELL_WIDTH = 38
    # CELL_HEIGHT = 41
    #
    # root = Tk()
    # root.geometry(f'{WIDTH * CELL_WIDTH}x{HEIGHT * CELL_HEIGHT}')
    # root.maxsize(WIDTH * CELL_WIDTH, HEIGHT * CELL_HEIGHT)
    # root.minsize(WIDTH * CELL_WIDTH, HEIGHT * CELL_HEIGHT)
    #
    # field = set_field(WIDTH, HEIGHT, root)
    # set_mines(MINES, field)
    # set_numbers(field)
    # # print(field)
    # print(field[0][0].r_cnt)
    # root.mainloop()
