import time
import math
import json
import numpy as np
from .board import *
from .node import *

HUMAN = 1
COMPUTER = 2

#!TODO
def solve(data): 
    """засекли время"""
    start_time = time.time()

    field = np.reshape(np.array(data['field']), (3, 3))
    move = data['move']
    

    print("\n--- %s seconds ---" % (time.time() - start_time))




def main():
    field = np.zeros((3, 3), dtype=np.int8)

    field[1][1] = HUMAN
    board = Board(field, COMPUTER)
    node = Node(board)

    print(node.board.field)
    node.evaluate(8)
    print('\n')
    print(node.pref_move.board.previous_turn)

    print('\n')

if __name__ == "__main__":
    main()