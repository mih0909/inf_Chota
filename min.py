from tkinter import *
from random import randint



class Game:


    CELL_WIDTH = 38
    CELL_HEIGHT = 41

    def __init__(self, width, height, mines):
        self.WIDTH = width
        self.HEIGHT = height
        self.MINES = mines
        self.root = Tk()

        self.root.geometry(f'{self.WIDTH * self.CELL_WIDTH}x{self.HEIGHT * self.CELL_HEIGHT}')
        self.root.maxsize(self.WIDTH * self.CELL_WIDTH, self.HEIGHT * self.CELL_HEIGHT)
        self.root.minsize(self.WIDTH * self.CELL_WIDTH, self.HEIGHT * self.CELL_HEIGHT)

        field = self.set_field()
        self.set_mines(field)
        self.set_numbers(field)
        self.root.mainloop()

    def set_field(self):
        mines = [[Mine(_master=self.root, _x=x, _y=y) for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        return mines

    def set_mines(self, lst: list):
        for i in range(self.MINES):
            a = lst[randint(0, len(lst[0]) - 1)][randint(0, len(lst) - 1)]
            a.set_mine()

    def set_numbers(self, field):
        y_e = len(field)
        x_e = len(field[0])
        for y in range(y_e):
            for x in range(x_e):
                env = [
                    [None, field[(y - 1) % y_e][(x - 1) % x_e]][0 <= y - 1 < y_e and 0 <= x - 1 < x_e],
                    [None, field[(y - 1) % y_e][(x + 0) % x_e]][0 <= y - 1 < y_e and 0 <= x + 0 < x_e],
                    [None, field[(y - 1) % y_e][(x + 1) % x_e]][0 <= y - 1 < y_e and 0 <= x + 1 < x_e],
                    [None, field[(y + 0) % y_e][(x - 1) % x_e]][0 <= y + 0 < y_e and 0 <= x - 1 < x_e],
                    [None, field[(y + 0) % y_e][(x + 1) % x_e]][0 <= y + 0 < y_e and 0 <= x + 1 < x_e],
                    [None, field[(y + 1) % y_e][(x - 1) % x_e]][0 <= y + 1 < y_e and 0 <= x - 1 < x_e],
                    [None, field[(y + 1) % y_e][(x + 0) % x_e]][0 <= y + 1 < y_e and 0 <= x + 0 < x_e],
                    [None, field[(y + 1) % y_e][(x + 1) % x_e]][0 <= y + 1 < y_e and 0 <= x + 1 < x_e],
                ]
                field[y][x].check_around(env)
                if field[y][x].is_bomb:
                    field[y][x].set_numbers()


class Mine:

    def __init__(self, _master, _x, _y, ):
        self.btn = Button(master=_master, width=4, height=2, bg='white',)
        self.btn.grid(row=_y, column=_x)
        self.is_bomb = False
        self.r_cnt = 0
        self.btn.config(command=self.on_clic)
        self.round = [None] * 8
        self.opened = False
        self.root = _master

    def set_mine(self):
        self.is_bomb = True
        # self.btn.config(bg="red")

    def check_around(self, lst: list):
        self.round = lst[:]

    def set_numbers(self):
        for cell in self.round:
            if cell and not cell.is_bomb:
                # cell.btn.config(bg='green')
                cell.r_cnt += 1

    def on_clic(self):
        colors = ['#AA00AA', '#191970', '#00BFFF', '#00FFFF', '#00FF7F']
        if self.is_bomb:
            self.detonate()
        self.btn.config(text=f'{self.r_cnt}', fg=colors[self.r_cnt], bg='gray')
        self.open()
        pass

    def detonate(self):
        self.end = Toplevel(self.root)
        btn = Button(master=self.end, text='close', command=self.restart)
        btn.pack()
        self.end.mainloop()

    def open(self):
        if self.opened:
            return
        if self.r_cnt == 0:
            for cell in self.round:
                if cell:
                    self.opened = True
                    cell.on_clic()

    def restart(self):
        self.end.destroy()
        self.root.destroy()
        game = Game(5, 5, 2)


if __name__ == '__main__':

    game = Game(15, 15, 1)

