import copy


class Options:
    def __init__(self):
        self.gamers = [0, 0]
        self.score = [0, 0]
        self.move_turn_start = 0


class Gamer:
    def __init__(self, char):
        self.GAMER_AI = 2
        self.GAMER_HUMAN = 1
        self.CHAR = char
        self.GAMER_DICT = {self.GAMER_HUMAN: 'Человек', self.GAMER_AI: 'ИИ'}

        print('Игрок ', self.CHAR)
        for i in self.GAMER_DICT:
            print(str(i) + '. ' + self.GAMER_DICT[i])
        self.gamer_class = int(input())

    def __str__(self):
        return self.GAMER_DICT[self.gamer_class]

    def move(self, field, ai, gamer_id, train):
        i = 0
        j = 0
        if self.gamer_class == self.GAMER_HUMAN:
            move_legal = False
            while not move_legal:
                i, j = map(int, input('№ строки № столбца\n').split())
                move_legal = field.move_legal(i, j)
        else:
            i, j = ai.move(field, gamer_id + 1, train)
        return i, j


class Field:
    def __init__(self):
        self.N = 3
        self.CHAR = [' ', 'X', 'O']

        self.field = None

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

    def cells_legal(self):
        cells_legal_list = []
        for i in range(self.N):
            for j in range(self.N):
                if self.field[i][j] == 0:
                    cells_legal_list.append([i, j])
        print(cells_legal_list)
        return cells_legal_list

    def cells_to_x(self, gamer):
        x = []
        for i in range(self.N):
            for j in range(self.N):
                if self.field[i][j] == 0:
                    x.extend((1, 0, 0))
                elif self.field[i][j] == gamer:
                    x.extend((0, 1, 0))
                else:
                    x.extend((0, 0, 1))
        print(x)
        return x

    def move_legal(self, i, j):
        if self.field[i][j] == 0:
            legal = True
        else:
            legal = False
        return legal

    def round_over_check(self):
        over = True
        gamer = 0
        field_transposed = list(map(list, zip(*self.field)))
        field_diagonals = [[], []]
        for i in range(self.N):
            field_diagonals[0].append(self.field[i][i])
            field_diagonals[1].append(self.field[i][self.N - 1 - i])
        for i in range(1, 3):
            for j in self.field:
                if j.count(i) == self.N:
                    gamer = i
                    break
            for j in field_transposed:
                if j.count(i) == self.N:
                    gamer = i
                    break
            for j in field_diagonals:
                if j.count(i) == self.N:
                    gamer = i
                    break
        if gamer == 0:
            for i in self.field:
                if 0 in i:
                    over = False
                    break
        return over, gamer


class Move:
    def __init__(self, field, cell, gamer):
        self.FIELD = field
        self.CELL = cell
        self.GAMER = gamer

    def __str__(self):
        return 'Игровое поле:\n ' +\
            str(self.FIELD) + 'Ход: ' +\
            str(self.CELL) + '\n' +\
            'Игрок: ' + str(self.GAMER) + '\n'

    def get_x(self):
        x = self.FIELD.cells_to_x(self.GAMER)
        for i in self.CELL:
            match i:
                case 0:
                    x.extend((1, 0, 0))
                case 1:
                    x.extend((0, 1, 0))
                case 2:
                    x.extend((0, 0, 1))
        return x


class Game:
    def __init__(self, ai, ai_train):
        self.AI_TRAIN = ai_train
        self.GAMERS = [Gamer('X'), Gamer('O')]
        self.TURN_MOVE_START = int(input('Кто ходит первым? (X - 1 / O - 2) ')) - 1

        self.ai = ai
        self.field = Field()
        self.score = [0, 0]
        self.turn_move_current = self.TURN_MOVE_START
        self.turn_move_round = self.turn_move_current
        self.moves = []

    @staticmethod
    def turn_move_change(turn_move):
        if turn_move == 0:
            turn_move = 1
        else:
            turn_move = 0
        return turn_move

    def __str__(self):
        return '%s %s:%s %s \n %s' % (self.GAMERS[0], self.score[0], self.score[1], self.GAMERS[1], self.field)

    def start(self):
        game_next = True
        while game_next:
            self.round_start()
            game_next = (int(input('Играть еще раз? (1 - Да / 2 - Нет) ')) == 1)
            if game_next == 1:
                self.round_new()
            else:
                self.finish()

    def finish(self):
        pass

    def round_start(self):
        self.field.clear()
        self.turn_move_current = self.turn_move_round
        self.round()

    def round(self):
        round_end = False
        while not round_end:
            print(self)
            field = copy.deepcopy(self.field)
            accept = False
            while not accept:
                cell = self.GAMERS[self.turn_move_current].move(self.field,
                                                                self.ai,
                                                                self.turn_move_current, self.AI_TRAIN)
                if self.AI_TRAIN and self.GAMERS[self.turn_move_current].gamer_class == self.GAMERS[self.turn_move_current].GAMER_AI:
                    print('Ход: ', cell)
                    confirm = int(input('Принять ход? (Да - 1 / Нет - 2)\n'))
                    if confirm == 1:
                        accept = True
                        y_real = 1
                    else:
                        y_real = -1
                    self.MOVE = Move(field, cell, self.turn_move_current)
                    x = self.MOVE.get_x()
                    y = self.ai.neural_net.activate(x)
                    self.ai.study(x, y, y_real)
                else:
                    accept = True
            self.field.move(self.turn_move_current, *cell)
            self.moves.append(Move(field, cell, self.turn_move_current))
            print(self.moves[-1])
            self.turn_move_current = self.turn_move_change(self.turn_move_current)
            round_end, gamer = self.field.round_over_check()
            if round_end:
                self.round_over(gamer)

    def round_over(self, gamer):
        if gamer == 0:
            result = 'Ничья'
        else:
            self.score[gamer - 1] += 1
            result = 'Победил %s %s\n' % (self.GAMERS[gamer - 1], self.GAMERS[gamer - 1].CHAR)
        # if self.AI_TRAIN:
        #     print('Учится ' + str(self.ai))
        #     self.ai_study(gamer - 1)
        print(self)
        print(result)

    def round_new(self):
        self.moves = []
        self.turn_move_round = self.turn_move_change(self.turn_move_round)

    def ai_study(self, gamer):
        for i in reversed(self.moves):
            print(i)
            x = i.get_x()
            print('x=', x)
            y = self.ai.neural_net.activate(x)
            if gamer == i.GAMER or gamer == -1:
                y_real = 1
            else:
                y_real = -1
            print('y=', y, 'y_real=', y_real)
            self.ai.study(x, y, y_real)
