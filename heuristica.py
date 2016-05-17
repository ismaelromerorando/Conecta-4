from utils import *
import games


def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]


def facil(state):
    if state.utility == 1 and state.to_move == 'O':
        return infinity
    if state.utility == -1 and state.to_move == 'X':
        return -infinity
    else:
        return 0


def medio(state):
    if state.utility == 1 and state.to_move == 'O':
        return infinity
    if state.utility == -1 and state.to_move == 'X':
        return -infinity
    else:
        return random.randint(-100, 100)


def dificil(state):
    heu=0

    if state.utility == 1 and state.to_move == 'O':
        return infinity
    if state.utility == -1 and state.to_move == 'X':
        return -infinity
    else:
        mov = legal_moves(state)

        for x in mov:
            heu = k_in_row(state.board, x, (0, 1), 'X') + \
                  k_in_row(state.board, x, (1, 0), 'X') + \
                  k_in_row(state.board, x, (1, -1),'X') + \
                  k_in_row(state.board, x, (1, 1),'X') - \
                  k_in_row(state.board, x, (0, 1), 'O') - \
                  k_in_row(state.board, x, (1, 0), 'O') - \
                  k_in_row(state.board, x, (1, -1),'O') - \
                  k_in_row(state.board, x, (1, 1),'O')

        return heu


def k_in_row(board, move, (delta_x, delta_y), player):

    x, y = move
    n = 0
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    while board.get((x, y)) == None and (x <= 7 and y <= 6 and x >= 1 and y >= 1):
        n += 0.5
        x, y = x + delta_x, y + delta_y
    x, y = move
    x, y = x - delta_x, y - delta_y
    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y
    while board.get((x, y)) == None and (x <= 7 and y <= 6 and x >= 1 and y >= 1):
        n += 0.5
        x, y = x - delta_x, y - delta_y
    return n






