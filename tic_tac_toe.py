class Gamer:
    def __init__(self, char):
        self.CHAR = char
        self.GAMER_DICT = {1: 'Человек', 2: 'ИИ'}

        print('Игрок ', self.CHAR)
        for i in self.GAMER_DICT:
            print(str(i) + '. ' + self.GAMER_DICT[i])
        self.gamer_class = int(input())

    def __str__(self):
        return self.GAMER_DICT[self.gamer_class]

    def move(self, field):
        i = 0
        j = 0
        if self.gamer_class == 1:
            move_legal = False
            while not move_legal:
                i, j = map(int, input('№ строки № столбца\n').split())
                move_legal = field.move_legal(i, j)
        return i, j


class Field:
    def __init__(self):
        self.N = 3
        self.CHAR = [' ', 'X', 'O']

        self.field = [[0 for j in range(self.N)] for i in range(self.N)]

    def __str__(self):
        field = '  0  1  2\n'
        for i in range(self.N):
            field += str(i) + ' '
            for j in range(self.N):
                field += ' ' + self.CHAR[self.field[i][j]] + ' '
            field += '\n'
        return field

    def move(self, gamer, i, j):
        self.field[i][j] = gamer

    def move_legal(self, i, j):
        if self.field[i][j] == 0:
            res = True
        else:
            res = False
        return res

    def game_over(self, score):
        end = True
        score = [5, 5]
        for i in range(self.N):
            for j in range(self.N):
                if self.field[i][j] == 0:
                    end = False
                    break
        return end


class Game:
    def __init__(self, field, gamers, score, turn_move_start):
        self.field = field
        self.gamers = gamers
        self.score = score
        self.turn_move_start = turn_move_start
        self.turn_current = self.turn_move_start

        self.game_move()

    def __str__(self):
        return '%s %s:%s %s \n %s' % (self.gamers[0], self.score[0], self.score[1], self.gamers[1], self.field)

    def game_move(self):
        print(self)
        while not self.field.game_over(self.score):
            self.field.move(self.turn_current + 1, *self.gamers[self.turn_current].move(self.field))
            if self.turn_current == 0:
                self.turn_current = 1
            else:
                self.turn_current = 0
            self.game_move()
