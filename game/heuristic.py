import numpy as np
HUMAN = 1
COMPUTER = 2

def score(consecutive, openEnds):
    """consecutive: общее количество последовательно стоящих фигур игрока на поле
       openEnds: общее количество открытых концов у игрока на поле"""

    if openEnds == 0 and consecutive < 5:
        return 0

    if consecutive == 4:
        if openEnds == 1:
            return 1000
        if openEnds == 2:
            return 1000

    if consecutive == 3:
        if openEnds == 1:
            return 7
        if openEnds == 2:
            return 100

    if consecutive == 2:
        if openEnds == 1:
            return 2
        if openEnds == 2:
            return 5

    if consecutive == 1:
        if openEnds == 1:
            return 0.5
        if openEnds == 2:
            return 1



def stringify(line):
    #* массив в строку
    s = str()
    for i in line:
        s += str(i)

    return s

def line_evaluation(line, player):
    #* получаем аргументом строку
    consecutive = 0
    open_ends = 0

    
    for i in range(4, 0, -1): 

        search_array = [player] * i
        search_string = stringify(search_array)
        index = line.find(search_string)
        
        if index == -1:
            continue

        rindex = index + len(search_string)

        if line[index - 1] == '0':
            open_ends += 1
        
        if rindex <= len(line) - 1:
            if line[rindex] == '0':
                open_ends += 1

        if open_ends != 0:
            consecutive = i
            print('consecutive = ', consecutive, '\nopen ends = ', open_ends)
            return score(consecutive, open_ends)

        #*если не нашел слева, начинает искать справа
        index = line.rfind(search_string)
        
        if index == -1:
            continue

        rindex = index + len(search_string)

        if line[index - 1] == '0':
            open_ends += 1
        
        if rindex <= len(line) - 1:
            if line[rindex] == '0':
                open_ends += 1

        if open_ends != 0:
            consecutive = i
            print('consecutive = ', consecutive, '\nopen ends = ', open_ends)

    return score(consecutive, open_ends)
    


def heuristic(field, player):
    horisontal = 0
    vertical = 0
    diagonal_right_left = 0
    diagonal_left_right = 0


    #* полсчет сверху вниз
    for row in field:
        horisontal += line_evaluation(stringify(row), player)
    
    #* подсчет справа налево
    for col in range(len(field)):
        vertical += line_evaluation(stringify(field[:, col]), player)

    #* подсчет диагонали справа налево
    temp = np.fliplr(field)
    for i in range(-18, 18, 1):
        diagonal_right_left += line_evaluation(stringify(temp.diagonal(i)), player)


    #* подсчет диагонали слева направо
    for i in range(-18, 18, 1):
        diagonal_left_right += line_evaluation(stringify(field.diagonal(i)), player)

    return horisontal + vertical + diagonal_left_right + diagonal_right_left
    


field = np.zeros((19, 19), dtype=np.int8)

test = np.array([[0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)

print(heuristic(test, HUMAN))


