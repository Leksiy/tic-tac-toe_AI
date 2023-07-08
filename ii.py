import random

class Perceptron:
    def __init__(self):
        self.w = [1, 1, 1, 1]
        self.T = 1

    def activate(self, x):
        res = self.w[0] * x[0] + self.w[1] * x[1] + self.w[2] * x[2] + self.w[3]
        if res >= T:
            res = 1
        else:
            res = -1


class CPU:
    def __init__(self):
        pass

    def move(self, field):
        legal_cell = []
        for i in range(field.N):
            for j in range(field.N):
                if field.field[i][j] == 0:
                    legal_cell.append([i, j])
        cell = random.choice(legal_cell)
        return cell