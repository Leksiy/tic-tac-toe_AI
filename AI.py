import random
import math
import copy


class Perceptron:
    def __init__(self, train_spped, function, x_count):
        self.TRAIN_SPEED = train_spped
        self.FUNCTION = function

        self.w = [1] * (x_count + 1)

    @staticmethod
    def sign(x):
        if x > 0:
            y = 1
        else:
            y = -1
        return y

    @staticmethod
    def sigmoid(x):
        y = round((1 / (1 + math.exp(-x))), 2)
        return y

    def activate(self, x):
        x_all = x.copy()
        x_all.append(1)
        y = 0
        for i, j in zip(x, self.w):
            y += i * j
        match self.FUNCTION:
            case 'sign':
                y = self.sign(y)
            case 'sigmoid':
                y = self.sigmoid(y)
        print('per.: ', x_all, self.w, y)
        return y

    def study(self, x, y, y_real):
        x_all = x.copy()
        x_all.append(1)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] + self.TRAIN_SPEED * (y_real - y) * x_all[i]

    def __str__(self):
        return ' '.join(map(str, self.w))


class NeuralNet:
    def __init__(self, name, level, perceptrons):
        self.NAME = name
        self.LEVEL = level

        self.perceptrons = []
        for i in range(self.LEVEL):
            self.perceptrons.append([])
            for j in range(perceptrons[i][0]):
                self.perceptrons[i].append(Perceptron(perceptrons[i][1], perceptrons[i][2], perceptrons[i][3]))

    def __str__(self):
        about = 'Тип нейросети: ' + self.NAME + '\n'
        about += 'Количество уровней: ' + str(self.LEVEL) + '\n'
        for i in range(self.LEVEL):
            about += 'Уровень ' + str(i + 1) + '\n'
            about += ' ' + 'Количество нейронов  - ' + str(len(self.perceptrons[i])) + '\n'
            about += ' ' + 'Количество дендритов - ' + str(len(self.perceptrons[i][0].w)) + '\n'
            about += ' ' + 'Скорость обучения    - ' + str(self.perceptrons[i][0].TRAIN_SPEED) + '\n'
            about += ' ' + 'Функция активации    - ' + str(self.perceptrons[i][0].FUNCTION) + '\n'
        return about

    def print_w(self):
        w = ''
        for i in range(self.LEVEL):
            for j in range(len(self.perceptrons[i])):
                w += 'Нейрон: ' + str(i) + '.' + str(j) + '\n'
                w += self.perceptrons[i][j].__str__() + '\n'
        return w

    def activate(self, x_real):
        x_next_level = x_real.copy()
        for i in range(self.LEVEL):
            y = []
            for j in range(len(self.perceptrons[i])):
                if j == 0:
                    x_perceptron = x_next_level[:len(self.perceptrons[i][j].w) - 1]
                    x_next_level = x_next_level[len(self.perceptrons[i][j].w) - 1:]
                    y.append(self.perceptrons[i][j].activate(x_perceptron))
                else:
                    y.append(self.perceptrons[i][j].activate(x_next_level))
            x_next_level = y.copy()
        return x_next_level[0]

    def study(self, x, y, y_real):
        self.perceptrons[0][0].study(x, y, y_real)


class Move:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)


class OptionsAI:
    def __init__(self):
        self.NEURAL_NET_TRAIN_SPEED = 1
        self.NEURAL_NETS = [NeuralNet('A', 1, [[1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 33]]),
                            NeuralNet('B', 3, [[33, self.NEURAL_NET_TRAIN_SPEED, 'sigmoid', 1],
                                               [33, self.NEURAL_NET_TRAIN_SPEED, 'sigmoid', 33],
                                               [1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 33]]),
                            NeuralNet('Test', 1, [[1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 3]])
                            ]

        self.train = True
        self.neural_nets_type = 0

    def __str__(self):
        res = ''
        if self.train:
            res += 'Включен,'
        else:
            res += 'Отключен,'
        res += ' тип:'
        res += ' ' + self.NEURAL_NETS[self.neural_nets_type].NAME
        return res

    def neural_nets_type_switch(self):
        self.neural_nets_type += 1
        if self.neural_nets_type not in range(len(self.NEURAL_NETS)):
            self.neural_nets_type = 0

    def on_off(self):
        self.train = not self.train

    def about(self):
        ai_about = str(self.NEURAL_NETS[self.neural_nets_type])
        return ai_about


class AI:
    def __init__(self, neural_net):
        self.neural_net = copy.deepcopy(neural_net)
        self.moves = []
        self.cells_legal_list = []
        self.x = []
        self.y = []

    def move(self, field, gamer):
        self.cells_legal_list = field.cells_legal()
        self.x = field.cells_to_x(gamer)
        self.y = []
        x_all = None
        print(self.neural_net.print_w())
        for i in self.cells_legal_list:
            x_all = self.x.copy()
            for j in i:
                match j:
                    case 0:
                        x_all.extend((1, 0, 0))
                    case 1:
                        x_all.extend((0, 1, 0))
                    case 2:
                        x_all.extend((0, 0, 1))
            y = self.neural_net.activate(x_all)
            print(x_all, y)
            self.y.append(y)
        cells_ai_list = []
        for i in range(len(self.y)):
            if self.y[i] == 1:
                cells_ai_list.append(self.cells_legal_list[i])
        if len(cells_ai_list) > 0:
            cell = random.choice(cells_ai_list)
        else:
            cell = random.choice(self.cells_legal_list)
        print(self.y, cells_ai_list, cell)
        self.moves.append(Move(x_all, 1 if cell in cells_ai_list else -1))
        print("\n".join(map(str, self.moves)))
        return cell

    def study(self, y_real):
        for i in self.moves:
            if i.y != y_real:
                self.neural_net.study(i.x, i.y, y_real)
                print(self.neural_net.print_w())
