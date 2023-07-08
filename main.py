import tic_tac_toe


class Game:
    def __init__(self):
        self.ii_train = True
        self.gamers = [0, 0]
        self.score = [0, 0]
        self.move_turn_start = 0

        self.main_menu()

    def main_menu(self):
        if self.ii_train:
            train_ii = 'Включен'
        else:
            train_ii = 'Отключен'
        print('1. Новая игра')
        print('2. Вкл./Откл. обучение ИИ - ' + train_ii)
        print('0. Выход')
        menu = int(input())
        match menu:
            case 0:
                self.game_exit()
            case 1:
                self.game_new()
            case _:
                self.ii_switch()

    def ii_switch(self):
        self.ii_train = not self.ii_train
        self.main_menu()

    def game_new(self):
        self.gamers = [tic_tac_toe.Gamer('X'), tic_tac_toe.Gamer('O')]
        self.score = [0, 0]
        self.move_turn_start = int(input('Кто ходит первым? (X - 1 / O - 2) ')) - 1

        game = tic_tac_toe.Game(self.gamers, self.score, self.move_turn_start)
        game.game_start()
        self.main_menu()

    def game_exit(self):
        pass


if __name__ == '__main__':
    app = Game()
