import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_counter, o_counter = 0, 0
    for row in board:
        for val in row:
            if val == X:
                x_counter += 1
            if val == O:
                o_counter += 1
    return X if x_counter == o_counter else O

def actions(board):
    moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves

def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise InvalidMove("Box is already filled!")
    new_board = deepcopy(board)
    new_board[i][j] = player(new_board)
    return new_board

def winner(board):
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] == X:
            return X
        if board[0][col] == board[1][col] == board[2][col] == O:
            return O
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    return all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    result = winner(board)
    if result == X:
        return 1
    if result == O:
        return -1
    return 0

def minimax(board):
    if terminal(board):
        return None
    return min_value(board)[1] if player(board) == O else max_value(board)[1]

def max_value(board):
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    best_move = None
    for action in actions(board):
        hypothetical_value = min_value(result(board, action))[0]
        if hypothetical_value > v:
            v = hypothetical_value
            best_move = action
    return [v, best_move]

def min_value(board):
    if terminal(board):
        return [utility(board), None]
    v = float('inf')
    best_move = None
    for action in actions(board):
        hypothetical_value = max_value(result(board, action))[0]
        if hypothetical_value < v:
            v = hypothetical_value
            best_move = action
    return [v, best_move]

class Error(Exception):
    pass

class InvalidMove(Error):
    def __init__(self, message):
        self.message = message

