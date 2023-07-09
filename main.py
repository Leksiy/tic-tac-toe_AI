import tic_tac_toe
import ii


class OptionsAI:
    def __init__(self):
        self.train = True
        self.type_dict = {0: 'A', 1: 'B'}
        self.type = 0

    def __str__(self):
        res = ''
        if self.train:
            res += 'Включен,'
        else:
            res += 'Отключен,'
        res += ' тип:'
        res += ' ' +  self.type_dict[self.type]
        return res

    def type_switch(self):
        self.type += 1
        if self.type not in self.type_dict:
            self.type = 0

    def on_off(self):
        self.train = not self.train

    def about(self):
        res = 'Тип ИИ: ' + self.type_dict[self.type]
        return res


class Options:
    def __init__(self):

        self.gamers = [0, 0]
        self.score = [0, 0]
        self.move_turn_start = 0


class Menu:
    def __init__(self):
        self.options_ai = OptionsAI()
        self.options = Options()

        self.menu_0()

    def menu_0(self):
        manu_exit = False
        while not manu_exit:
            print('1. Новая игра')
            print('2. Вкл./Откл. обучение ИИ - ' + str(self.options_ai))
            print('3. Выбор типа ИИ')
            print('4. Информация об ИИ')
            print('0. Выход')
            menu = int(input())
            match menu:
                case 1:
                    self.game_new()
                case 2:
                    self.ii_on_off()
                case 3:
                    self.ii_switch()
                case 4:
                    self.ii_about()
                case _:
                    manu_exit = self.game_exit()

    def game_new(self):
        self.gamers = [tic_tac_toe.Gamer('X', self.ii_train), tic_tac_toe.Gamer('O', self.ii_train)]
        self.score = [0, 0]
        self.move_turn_start = int(input('Кто ходит первым? (X - 1 / O - 2) ')) - 1

        game = tic_tac_toe.Game(self.gamers, self.score, self.move_turn_start)
        game.game_start()

    def ii_on_off(self):
        self.options_ai.on_off()

    def ii_switch(self):
        self.options_ai.type_switch()

    def ii_about(self):
        self.options_ai.about()

    def game_exit(self):
        return True


if __name__ == '__main__':
    app = Menu()
