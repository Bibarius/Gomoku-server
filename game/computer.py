import numpy as np
import time
import math
from board import *
from node import *


HUMAN = 1
COMPUTER = 2

start_time = time.time()

field = np.zeros((3, 3), dtype=np.int8)

field[1][1] = HUMAN


board = Board(field, COMPUTER)
node = Node(board)

print(node.board.field)
node.evaluate(8)
print('\n')
print(node.pref_move.board.previous_turn)

print('\n')

print("\n--- %s seconds ---" % (time.time() - start_time))
