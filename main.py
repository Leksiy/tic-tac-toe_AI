import tic_tac_toe
import AI


class Menu:
    def __init__(self):
        self.NEURAL_NET_TRAIN_SPEED = 0.5

        self.neural_nets = [AI.NeuralNet('A', 1, [[1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 33]]),
                            AI.NeuralNet('B', 2, [[33, self.NEURAL_NET_TRAIN_SPEED, 'sigmoid', 33],
                                                  [1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 33]]),
                            AI.NeuralNet('Test', 2, [[11, self.NEURAL_NET_TRAIN_SPEED, 'sigmoid', 33],
                                                     [1, self.NEURAL_NET_TRAIN_SPEED, 'sign', 11]]),
                            ]
        self.ai_neural_net_type = 0
        self.ai_train = True
        self.ai = None

        self.menu_0()

    def ai_train_state(self):
        res = ''
        if self.ai_train:
            res += 'Включен'
        else:
            res += 'Отключен'
        return res

    def neural_net_type_state(self):
        res = 'тип: ' + self.neural_nets[self.ai_neural_net_type].NAME
        return res

    def menu_0(self):
        menu_exit = False
        while not menu_exit:
            print('1. Новая игра')
            print('2. Вкл./Откл. обучение нейросети - ' + self.ai_train_state())
            print('3. Выбор типа нейросети - ' + self.neural_net_type_state())
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
        self.ai = AI.AI(self.neural_nets[self.ai_neural_net_type])
        game = tic_tac_toe.Game(self.ai, self.ai_train)
        game.start()

    def ai_on_off(self):
        self.ai_train = not self.ai_train

    def ai_switch(self):
        self.ai_neural_net_type += 1
        if self.ai_neural_net_type not in range(len(self.neural_nets)):
            self.ai_neural_net_type = 0

    def ai_about(self):
        print(str(self.neural_nets[self.ai_neural_net_type]))

    @staticmethod
    def game_exit():
        return True


if __name__ == '__main__':
    app = Menu()
