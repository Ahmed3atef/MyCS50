"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

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

    # set variables 
    x_count = 0
    o_count = 0

    # navigate around the board and count x , o or empty feilds 
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    
    # make make decision
    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # make set of available actions
    action_available = set()
    
    # navigate around cells and add empty cell to variable
    for row_index, row in enumerate(board):
        for column_index , cell in enumerate(row):
            if cell == EMPTY:
                action_available.add((row_index,column_index))
    
    # end of function
    return action_available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # first i need to know my current state
    player_move = player(board)

    # i copy all board in new varaible 
    new_board = deepcopy(board) 
    
    # action in this situation is position of action in the 2d array i for rows j for columns
    i,j = action

    # check action in board and merge action with state 
    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move
    
    # end of the function
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X,O):
        # verical
        for row in board:
            if row == [player] * 3:
                return player
        # horizontal
        for y in range(3):
            column =[board[x][y] for x in range(3)]
            if column == [player] * 3:
                return player
        #diagonal
        if [board[i][i] for i in range(0,3)] == [player] * 3:
            return player
        elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
            return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # if player win in this game
    if winner(board) != None:
        return True
    
    # check Empty cell
    for row in board:
        if EMPTY in row:
            return False

    # if all cells have been filled
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)

    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # max function wating min result
    def Max(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = Min(result(board,action))[0]
                if minval > v :
                    v =  minval
                    optimal_move = action
            return v, optimal_move

    # min function wating max result
    def Min(board):
        optimal_move = ()
        if terminal(board):
            return utility(board),optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = Max(result(board,action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    # If the board is a terminal board
    curtent_player = player(board)
    if terminal(board):
        return None

    # run min and max functions above
    if curtent_player == X:
        return Max(board)[1]
    else:
        return Min(board)[1]