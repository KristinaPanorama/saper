from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.init()

    def init(self):
        self.pole = [[Cell() for t in range(self.N)] for i in range(self.N)]
        counter = self.M
        while counter:
            a = randint(0, self.N-1)
            b = randint(0, self.N-1)
            if not self.pole[a][b].mine:
                self.pole[a][b].mine = True
                counter -= 1

        indxs = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    mines = sum([self.pole[i+x][j+y].mine for x, y in indxs
                                if 0 <= i+x <= self.N-1 and 0 <= j+y <= self.N-1])
                    self.pole[i][j].around_mines = mines
                else:
                    self.pole[i][j].mine = True

    def play(self):
        c = (self.N * self.N) - self.M
        while c:
            try:
                i, j = map(int, input(f'Введите 2 числа от 1 до {self.N} включительно: ').split())

            except:
                print('Неверный формат.')
                continue
            if i <1 and j< 1:
                continue
            cell = self.pole[i - 1][j - 1]
            if not cell.fl_open and not cell.mine:
                cell.fl_open = True
                self.show()
                c -= 1
            elif cell.mine:
                cell.fl_open = True
                self.game_over_show()
                print('Game over')
                break
        else:
            print('You win!')

    def show(self):
        for i in self.pole:
            for t in i:
                print('#' if t.fl_open == False else '*' if t.mine else t.around_mines,  end=' ')
            print()

    def game_over_show(self):
        for i in self.pole:
            for t in i:
                print(t.around_mines if not t.mine else '*', end=' ')
            print()


g = GamePole(3, 2)
g.show()
g.play()