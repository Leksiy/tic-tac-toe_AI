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
