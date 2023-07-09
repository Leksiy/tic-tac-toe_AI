import random


class Perceptron:
    def __init__(self, x_count):
        self.LAMBDA = 0.2

        self.w = [1 for i in range(x_count + 1)]

    def activate(self, x):
        x_all = x.copy()
        x_all.append(1)
        y = 0
        for i, j in zip(x, self.w):
            y += i * j
        if y > 0:
            y = 1
        else:
            y = -1
        return y

    def study(self, result, move):
        x = move.state.copy()
        x.append(1)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] + self.LAMDA * (result - move.result) * x[i]
        print(self.w)

    def __str__(self):
        return ' '.join(map(str, self.w))


class NeuralNet:
    def __init__(self, level, count):
        self. perceptrons = []
        for i in range(level):
            self.perceptrons.append([])
            for j in range(len(count[i])):
                self.perceptrons[i].append(Perceptron(count[i][j]))

    def __str__(self):
        perceptrons_list = ''
        for i in range(len(self.perceptrons)):
            perceptrons_list += '\n'.join(map(str, self.perceptrons[i]))
            perceptrons_list += '\n'
        return perceptrons_list

    def activate_A(self, x):
        y = self.perceptrons[0][0].activate(x)
        return y

    def activate_B(self, x):
        level_1 = []
        for i in range(len(x)):
            level_1.append(self.perceptrons[0][i].activate([x[i]]))
        level_2 = []
        for i in range(len(level_1)):
            level_2.append(self.perceptrons[1][i].activate(level_1))
        y = self.perceptrons[2][0].activate(level_2)
        return y

    def study_A(self, result, move):
        self.perceptrons[0][0].study(result, move)

    def study_B(self, result, move):
        for i in range(len(self.perceptrons[0])):
            level_1_move = Move(move.cell, [move.state[i]], move.result)
            self.perceptrons[0][i].study(result, level_1_move)
        for i in range(len(self.perceptrons[1])):
            self.perceptrons[1][i].study(result, move)
        self.perceptrons[2][0].study(result, move)


class Move:
    def __init__(self, cell, state, result):
        self.cell = cell
        self.state = state
        self.result = result

    def __str__(self):
        return str(self.cell) + ' ' + str(self.state) + ' ' + str(self.result)


class CPU:
    def __init__(self, class_neural_net):
        self.CLASS_NEURAL_NET = class_neural_net
        self.N = 3

        self.moves = []
        match self.CLASS_NEURAL_NET:
            case 'A':
                self.neural_net = [[NeuralNet(1, [[27]]) for i in range(self.N)] for j in range(self.N)]
            case 'B':
                self.neural_net = [[NeuralNet(3, [[1 for i in range(27)], [27 for i in range(27)], [27]]) for j in range(self.N)] for z in range(self.N)]

    def move(self, field):
        legal_cell = []
        cpu_cell = []
        state = []
        for i in range(field.N):
            for j in range(field.N):
                if field.field[i][j] == 1:
                    state.append(0)
                    state.append(1)
                    state.append(0)
                if field.field[i][j] == 2:
                    state.append(0)
                    state.append(0)
                    state.append(1)
                if field.field[i][j] == 0:
                    state.append(1)
                    state.append(0)
                    state.append(0)
                    legal_cell.append([i, j])
        for i in range(field.N):
            for j in range(field.N):
                if [i, j] in legal_cell:
                    if self.neural_net[i][j].activate_B(state) == 1:
                        cpu_cell.append([i, j])
        state_cell = cpu_cell.copy()
        print(state_cell)
        if len(cpu_cell) == 0:
            cpu_cell = legal_cell.copy()
        cell = random.choice(cpu_cell)
        if cell in state_cell:
            self.moves.append(Move(cell, state, 1))
        else:
            self.moves.append(Move(cell, state, -1))
        return cell

    def ii_train(self, result):
        for i in self.moves:
            if i.result != result:
                self.neural_net[i.cell[0]][i.cell[1]].study_B(result, i)
