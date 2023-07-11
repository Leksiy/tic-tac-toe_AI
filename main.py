import tic_tac_toe
import AI


class OptionsAI:
    def __init__(self):
        self.NEURAL_NET_TRAIN_SPEED = 0.2
        self.NEURAL_NETS = [AI.NeuralNet('A', 1, [[1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 33]]),
                            AI.NeuralNet('B', 3, [[33, self.NEURAL_NET_TRAIN_SPEED, 'sigmoid', 1],
                                                  [33, self.NEURAL_NET_TRAIN_SPEED, 'sigmoid', 33],
                                                  [1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 33]]),
                            AI.NeuralNet('Test', 1, [[1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 3]])
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
        res += ' ' +  self.NEURAL_NETS[self.neural_nets_type].NAME
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


class Menu:
    def __init__(self):
        self.N = tic_tac_toe.Field().N

        self.options_ai = OptionsAI()
        self.menu_0()


    def menu_0(self):
        menu_exit = False
        while not menu_exit:
            print('1. Новая игра')
            print('2. Вкл./Откл. обучение нейросети - ' + str(self.options_ai))
            print('3. Выбор типа нейросети')
            print('4. Информация об нейросети')
            print('0. Выход')
            menu = int(input())
            match menu:
                case 1:
                    self.game_new()
                case 2:
                    self.ai_on_off()
                case 3:
                    self.ai_switch()
                case 4:
                    self.ai_about()
                case _:
                    menu_exit = self.game_exit()

    def game_new(self):
        game = tic_tac_toe.Game(self.options_ai)
        game.start()
        # self.gamers = [tic_tac_toe.Gamer('X', self.ai_train), tic_tac_toe.Gamer('O', self.ai_train)]
        # self.score = [0, 0]
        # self.move_turn_start = int(input('Кто ходит первым? (X - 1 / O - 2) ')) - 1
        #
        # game = tic_tac_toe.Game(self.gamers, self.score, self.move_turn_start)
        # game.game_start()

    def ai_on_off(self):
        self.options_ai.on_off()

    def ai_switch(self):
        self.options_ai.neural_nets_type_switch()

    def ai_about(self):
        print(self.options_ai.about())

    def game_exit(self):
        return True


if __name__ == '__main__':
    app = Menu()
