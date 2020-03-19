import numpy as np

HUMAN = 1
COMPUTER = 2

class Board:
    def __init__(self, field, turn):
        self.field = field
        self.turn = turn
        self.previous_turn = []

    def evaluate(self):
        if self.winning(COMPUTER):
            return 100
        if self.winning(HUMAN):
            return -100
        else:
            return 0

    def next_turn(self):
        if self.turn == HUMAN:
            return COMPUTER
        else:
            return HUMAN

    def clone(self):
        new_field = np.copy(self.field)
        return Board(new_field, self.turn)

    def place_turn(self, y, x):
        temp = self.clone()
        temp.field[y][x] = temp.turn

        """Делаем так чтобы экземпляр доски в ноде хранил ход который привел к этому состоянию"""
        temp.previous_turn.append(y)
        temp.previous_turn.append(x)

        temp.turn = temp.next_turn()
        return temp

    def winning(self, player):
        if (
            (self.field[0][0] == player and self.field[0][1] == player and self.field[0][2] == player) or
            (self.field[1][0] == player and self.field[1][1] == player and self.field[1][2] == player) or
            (self.field[2][0] == player and self.field[2][1] == player and self.field[2][2] == player) or
            (self.field[0][0] == player and self.field[1][1] == player and self.field[2][2] == player) or
            (self.field[0][2] == player and self.field[1][1] == player and self.field[2][0] == player) or
            (self.field[0][0] == player and self.field[1][0] == player and self.field[2][0] == player) or
            (self.field[0][1] == player and self.field[1][1] == player and self.field[2][1] == player) or
            (self.field[0][2] == player and self.field[1]
             [2] == player and self.field[2][2] == player)
        ):
            return True