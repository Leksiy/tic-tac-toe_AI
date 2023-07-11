import tic_tac_toe
import AI


class Menu:
    def __init__(self):
        self.options_ai = AI.OptionsAI()
        self.ais = [AI.AI(self.options_ai.NEURAL_NETS[self.options_ai.neural_nets_type]),
                    AI.AI(self.options_ai.NEURAL_NETS[self.options_ai.neural_nets_type])]
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
        game = tic_tac_toe.Game(self.options_ai, self.ais)
        game.start()

    def ai_on_off(self):
        self.options_ai.on_off()

    def ai_switch(self):
        self.options_ai.neural_nets_type_switch()
        for i in self.ais:
            i = AI.AI(self.options_ai.NEURAL_NETS[self.options_ai.neural_nets_type])

    def ai_about(self):
        print(self.options_ai.about())

    @staticmethod
    def game_exit():
        return True


if __name__ == '__main__':
    app = Menu()
