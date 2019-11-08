from board import *


class Node:
    def __init__(self, board):
        self.board = board
        self.childs = []

        self.alpha = -10000000
        self.beta = 1000000

        """Эвристическая оценка данного узла"""
        self.current_eval = 0

        """Выбранный следующий ход для данного узла"""
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

                evaluate = i.board.evaluate()
                if evaluate == 100 or -100:
                    self.current_eval = evaluate
                    self.pref_move = i

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