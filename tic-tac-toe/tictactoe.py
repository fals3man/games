import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0
    for row in board:
        numX += row.count(X)
        numO += row.count(O)

    # Next player is the one with the fewest moves currently
    if numX > numO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    legal_actions = set()
    for row in range(3):
        for cell in range(3):
            if board[cell][row] == EMPTY:
                legal_actions.add((row, cell))

    return legal_actions
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action[0] not in range(0, 3) or action[1] not in range(0, 3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for mark in [X, O]:
        
        for row in range(0, 3):
            if all(board[row][col]==mark for col in range(0, 3)):
                return mark
        
        for col in range(0, 3):
            if all(board[row][col]==mark for row in range(0, 3)):
                return mark

        diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for diagonal in diagonals:
            if all(board[row][col]==mark for (row, col) in diagonal):
                return mark

    return None

        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or not actions(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    if board ==initial_state():
        return 0,1    

    if player(board) == X:
        best_v = -math.inf
        for move in actions(board):
            max_v = minimax_value(result(board, move),best_v)
            if max_v > best_v:
                best_v = max_v
                best_move = move
    
    elif player(board) == O:
        best_v = math.inf
        for move in actions(board):
            min_v = minimax_value(result(board, move),best_v) 
            if min_v < best_v:
                best_v = min_v
                best_move = move
    return best_move 


def minimax_value(board,best_v):
    """
    Returns the minimum utility of the current board.
    """

    if terminal(board):
        return utility(board)
    
    v=float("-inf") if player(board) ==X else float ("inf")

    for move in actions(board):
        new_v = minimax_value(result(board, move),v)
        if player(board)==X:
            if new_v>best_v:
                return new_v
            v=max(v,new_v)
        if player(board)==O:
            if new_v<best_v:
                return new_v
            v=min(v,new_v)        
    return v