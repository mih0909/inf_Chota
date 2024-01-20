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
        print(field[0][0].r_cnt)
        root.mainloop()

class Mine:

    def __init__(self, _master, _x, _y, ):
        self.btn = Button(master=_master, width=4, height=2, bg='gray',)
        self.btn.grid(row=_y, column=_x)
        self.is_bomb = False
        self.r_cnt = 0
        self.btn.config(command=self.on_clic())

    def set_mine(self):
        self.is_bomb = True
        self.btn.config(bg="red")

    def check_around(self, lst: list):
        for i in range(len(lst)):
            if lst[i].is_bomb:
                continue
            lst[i].r_cnt += 1
            lst[i].btn.config(text=f'{lst[i].r_cnt}')
            # cell.btn.config(bg='blue')


    def on_clic(self):
        # self.btn.config(text=f'{self.r_cnt}')
        # self.btn.destroy()
        pass

def set_field(width, height, master):
    mines = [[Mine(_master=master, _x=x, _y=y) for x in range(width)] for y in range(height)]
    return mines


def set_mines(m_cnt: int, lst: list):
    for i in range(m_cnt):
        a = lst[randint(0, len(lst)-1)][randint(0, len(lst[0])-1)]
        a.set_mine()


def set_numbers(field):
    for x in range(len(field)):
        for y in range(len(field[0])):
            if field[x][y].is_bomb:
                round = []
                for i in range(-1, 2):
                    for j in range(-1,2):
                        if x+i < 0 or y+j < 0 or (i == 0 and j == 0):
                            continue
                        else:
                            try:
                                round.append(field[x+i][y+j])
                            except Exception:
                                continue
                field[x][y].check_around(round)


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
