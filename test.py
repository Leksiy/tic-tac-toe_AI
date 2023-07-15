class test:
    def __init__(self, ai):
        self.ai = ai

    def start_test(self):
        next = True
        while next:
            x = list(map(int, input('x = ').split()))
            y = self.ai.activate(x)
            y_real = int(input('y = '))
            self.ai.study(x, y, y_real)
            then_end = int(input('Завершить тест? (Да - 1 / Нет - 2)\n'))
            if then_end == 1:
                next = False