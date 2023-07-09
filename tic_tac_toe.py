class Gamer:
    def __init__(self, char, ii_train):
        self.CHAR = char
        self.GAMER_DICT = {1: 'Человек', 2: 'ИИ'}
        self.CPU = ii.CPU('B')
        self.II_TRAIN = ii_train

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
        else:
            i, j = self.CPU.move(field)
        return i, j

    def ii_train(self, result):
        if self.gamer_class == 2 and self.II_TRAIN:
            self.CPU.ii_train(result)


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

    def clear(self):
        self.field = [[0 for j in range(self.N)] for i in range(self.N)]

    def move(self, gamer, i, j):
        self.field[i][j] = gamer + 1

    def move_legal(self, i, j):
        if self.field[i][j] == 0:
            legal = True
        else:
            legal = False
        return legal

    def game_over(self):
        end = True
        gamer = 0
        field_t = list(map(list, zip(*self.field)))
        field_d = [[], []]
        for i in range(self.N):
            field_d[0].append(self.field[i][i])
            field_d[1].append(self.field[i][self.N -1 -i])
        for i in self.field:
            if i.count(1) == self.N:
                gamer = 1
                break
            if i.count(2) == self.N:
                gamer = 2
                break
        for i in field_t:
            if i.count(1) == self.N:
                gamer = 1
                break
            if i.count(2) == self.N:
                gamer = 2
                break
        for i in field_d:
            if i.count(1) == self.N:
                gamer = 1
                break
            if i.count(2) == self.N:
                gamer = 2
                break
        if gamer == 0:
            for i in self.field:
                if 0 in i:
                    end = False
                    break
        return end, gamer


class Game:
    def __init__(self, gamers, score, turn_move_start):
        self.GAMERS = gamers

        self.field = Field()
        self.score = score
        self.turn_move_start = turn_move_start
        self.turn_move_current = self.turn_move_start

    def turn_change(self):
        if self.turn_move_current == 0:
            self.turn_move_current = 1
        else:
            self.turn_move_current = 0

    def turn_start_change(self):
        if self.turn_move_start == 0:
            self.turn_move_start = 1
        else:
            self.turn_move_start = 0

    def game_start(self):
        self.field.clear()
        self.game_move()

    def game_new(self):
        self.GAMERS[0].CPU.moves = []
        self.GAMERS[1].CPU.moves = []
        self.turn_start_change()
        self.turn_move_current = self.turn_move_start
        self.game_start()

    def game_end(self):
        pass

    def game_over(self):
        end, gamer = self.field.game_over()
        result = ''
        if end:
            if gamer == 0:
                result = 'Ничья'
            else:
                self.score[gamer - 1] += 1
                result = 'Победил %s %s\n' % (self.GAMERS[gamer - 1], self.GAMERS[gamer - 1].CHAR)
                if gamer == 1:
                    self.GAMERS[0].ii_train(1)
                    self.GAMERS[1].ii_train(-1)
                elif gamer == 2:
                    self.GAMERS[0].ii_train(-1)
                    self.GAMERS[1].ii_train(1)
            print(self)
            print(result)
            next_game = int(input('Играть еще раз? (1 - Да / 2 - Нет) '))
            if next_game == 1:
                self.game_new()
            else:
                self.game_end()
        else:
            self.game_move()

    def __str__(self):
        return '%s %s:%s %s \n %s' % (self.GAMERS[0], self.score[0], self.score[1], self.GAMERS[1], self.field)

    def game_move(self):
        print(self)
        self.field.move(self.turn_move_current, *self.GAMERS[self.turn_move_current].move(self.field))
        self.turn_change()
        self.game_over()
