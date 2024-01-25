from tkinter import *
from random import randint


global field


class Game:

    CELL_WIDTH = 38
    CELL_HEIGHT = 41
    empty_cells = 0

    @staticmethod
    def compare():
        if Mine.remain == Game.empty_cells:
            Mine.detonate(ending='Победа')

    def __init__(self, width, height, mines):

        global field
        self.WIDTH = width
        self.HEIGHT = height
        self.MINES = mines
        Game.empty_cells = width * height - mines

        self.root = Tk()
        self.root.geometry(f'{self.WIDTH * self.CELL_WIDTH}x{self.HEIGHT * self.CELL_HEIGHT}+'
                           f'{self.root.winfo_screenwidth()//3}+{self.root.winfo_screenheight()//3}')
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
            cell = lst[randint(0, len(lst[0]) - 1)][randint(0, len(lst) - 1)]
            while cell.is_bomb:
                cell = lst[randint(0, len(lst[0]) - 1)][randint(0, len(lst) - 1)]
            cell.set_mine()

    def set_numbers(self, mine_field,):
        y_e = len(mine_field)
        x_e = len(mine_field[0])
        for y in range(y_e):
            for x in range(x_e):
                env = [
                    [None, mine_field[(y - 1) % y_e][(x - 1) % x_e]][0 <= y - 1 < y_e and 0 <= x - 1 < x_e],
                    [None, mine_field[(y - 1) % y_e][(x + 0) % x_e]][0 <= y - 1 < y_e and 0 <= x + 0 < x_e],
                    [None, mine_field[(y - 1) % y_e][(x + 1) % x_e]][0 <= y - 1 < y_e and 0 <= x + 1 < x_e],
                    [None, mine_field[(y + 0) % y_e][(x - 1) % x_e]][0 <= y + 0 < y_e and 0 <= x - 1 < x_e],
                    [None, mine_field[(y + 0) % y_e][(x + 1) % x_e]][0 <= y + 0 < y_e and 0 <= x + 1 < x_e],
                    [None, mine_field[(y + 1) % y_e][(x - 1) % x_e]][0 <= y + 1 < y_e and 0 <= x - 1 < x_e],
                    [None, mine_field[(y + 1) % y_e][(x + 0) % x_e]][0 <= y + 1 < y_e and 0 <= x + 0 < x_e],
                    [None, mine_field[(y + 1) % y_e][(x + 1) % x_e]][0 <= y + 1 < y_e and 0 <= x + 1 < x_e],
                ]
                mine_field[y][x].check_around(env)
                if mine_field[y][x].is_bomb:
                    mine_field[y][x].set_r_cnt()


class Mine:

    remain = 0
    root = None
    end = None

    def __init__(self, _master, _x, _y, ):
        self.btn = Button(master=_master, width=4, height=2, bg='#808080',)
        self.btn.grid(row=_y, column=_x)
        self.is_bomb = False
        self.r_cnt = 0
        self.btn.config(command=lambda: [self.on_clic(), Game.compare()])
        self.round = [None] * 8
        self.opened = False
        Mine.root = _master

    def set_mine(self):
        self.is_bomb = True
        # self.btn.config(bg="red")

    def check_around(self, lst: list):
        self.round = lst[:]

    def set_r_cnt(self):
        for cell in self.round:
            if cell and not cell.is_bomb:
                # cell.btn.config(bg='green')
                cell.r_cnt += 1

    def on_clic(self):
        if not self.opened:
            Mine.remain += 1
        self.opened = True
        self.open()
        if self.is_bomb:
            Mine.detonate()
        if self.r_cnt == 0:
            for cell in self.round:
                if cell and not cell.opened:
                    cell.on_clic()
        pass

    def open(self):
        colors = ['#000000', '#f53c2c', '#0000FF', '#005AFF', '#8B00FF', '#00FF7F']
        if self.r_cnt != 0:
            self.btn.config(text=f'{self.r_cnt}', fg=colors[self.r_cnt])
        self.btn.config(bg='#ABABAB')
        pass

    @staticmethod
    def detonate(ending='НЕ ПОБЕДА'):
        Mine.block()
        Mine.remain = 0
        Mine.end = Toplevel(Mine.root)
        Mine.end.title(ending)
        Mine.end.geometry(f'{Mine.root.geometry()}')
        btn = Button(master=Mine.end, text='restart\n15x15',
                     command=lambda: Mine.restart(15, 15, 20), width=6, height=3)
        btn.grid(row=0, column=0)
        btn = Button(master=Mine.end, text='restart\n9x9',
                     command=lambda: Mine.restart(9, 9, 9), width=6, height=3)
        btn.grid(row=0, column=1)
        btn = Button(master=Mine.end, text='restart\n5x5',
                     command=lambda: Mine.restart(5, 5, 3), width=6, height=3)
        btn.grid(row=0, column=2)
        Mine.end.mainloop()

    @staticmethod
    def restart(w, h, m):
        Mine.end.destroy()
        Mine.root.destroy()
        Game(width=w, height=h, mines=m)

    @staticmethod
    def block():
        global field
        for i in field:
            for j in i:
                j.btn['state'] = 'disabled'


if __name__ == '__main__':
    game = Game(15, 15, 1)
