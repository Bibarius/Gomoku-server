import numpy as np
import time
import math

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


class Node:
    def __init__(self, board):
        self.board = board
        self.childs = []

        self.alpha = -10000000
        self.beta = 1000000

        self.current_eval = 0
        self.pref_move = 0

    def add_child(self, board):
        node = Node(board)
        self.childs.append(node)

    def fill_childs(self):
        for row in range(len(self.board.field)):
            for cell in range(len(self.board.field[row])):
                if self.board.field[row][cell] == 0:
                    self.add_child(self.board.place_turn(row, cell))
                else:
                    continue

    def min_child(self):  # ! Находим минимальное из детей
        min = self.childs[0]
        for i in self.childs:
            if i.current_eval <= min.current_eval:
                min = i
        return min

    def max_child(self):  # ! Находим максимальное из детей
        max = self.childs[0]
        for i in self.childs:
            if i.current_eval >= max.current_eval:
                max = i
        return max

    def max_board(self):
        max = -1000000
        for i in self.childs:
            if i.board.evaluate() > max:
                max = i.board.evaluate()
        return max

    def min_board(self):
        min = 1000000
        for i in self.childs:
            if i.board.evaluate() > min:
                min = i.board.evaluate()
        return min

    def evaluate(self, depth, alpha=-1000000, beta=1000000):

        self.alpha = alpha
        self.beta = beta
        self.fill_childs()

        if len(self.childs) == 0:
            self.current_eval = 0
            return

        if depth != 0:
            for i in self.childs:

                if i.board.evaluate() == 100:
                    self.current_eval = 100
                    self.pref_move = i
                    return

                if i.board.evaluate() == -100:
                    self.current_eval = -100
                    self.pref_move = i
                    return


                i.evaluate(depth - 1, self.alpha, self.beta)
                
                #! Альфа бета отсечение
                if self.board.turn == COMPUTER:
                    if i.current_eval >= self.alpha:
                        self.alpha = i.current_eval
                else:
                    if i.current_eval <= self.beta:
                        self.beta = i.current_eval

                if self.alpha >= self.beta:
                    break



            if self.board.turn == COMPUTER:
                self.pref_move = self.max_child()
                self.current_eval = self.pref_move.current_eval
            else:
                self.pref_move = self.min_child()
                self.current_eval = self.pref_move.current_eval
        else:
            if self.board.turn == COMPUTER:
                self.current_eval = self.max_board()
            else:
                self.current_eval = self.min_board()


start_time = time.time()

field = np.zeros((3, 3), dtype=np.int8)

field[1][1] = HUMAN





board = Board(field, COMPUTER)
node = Node(board)

print(node.board.field)
node.evaluate(10)
print('\n')
print(node.pref_move.board.previous_turn)

print('\n')

print("\n--- %s seconds ---" % (time.time() - start_time))
