"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None

Winner = None
act = None

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

    if(terminal(board) == True):    # if the game is over return 
        return X                # or O dosent matter

    xcount = 0
    ocount = 0
    #ecount = 0

    for i in board:
        for j in i:
            if(j == X):
                xcount += 1
            elif(j == O):
                ocount += 1
            #elif(j == EMPTY):
            #    ecount += 1

    if(xcount > ocount):   # if x has moved
        return O
    elif(xcount == ocount):
        return X            # if o has moved
    #elif(ecount == 0):
    #    return X        # or O dosent matter b/c board filled       // may not be needed due to terminal call at beginning of function


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if(terminal(board) == True):    # if board is finished return 0,0
        return {(0,0)}
    
    retSet = set()                      # create empty set
    length = len(board[0])

    for i in range(length):
        for j in range(length):
            if(board[i][j] != X and board[i][j] != O):      # if there is not x or o add index to set
                retSet.add((i, j))

    return retSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if(not isinstance(action, tuple)):           # if action not valid, raise error
        raise ValueError

    copyboard = copy.deepcopy(board)        # deep copy the board
    playerTurn = player(board)              # get players turn 

    copyboard[action[0]][action[1]] = playerTurn    # set action to player turn

    return copyboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    gameover = terminal(board)

    if(gameover == False or Winner == EMPTY or Winner == None):
        return None
    elif(Winner == X):
        return X
    elif(Winner == O):
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    length = len(board[0])
    ecount = 0
    play = None
    global Winner
    
    for i in board:     # for each row
        row = True

        for j in range(len(i)):     
            play = i[0]         # get the first item in row to compare rest of row to

            if(play == None):
                row = False
                continue

            if(i[j] != play):   # see if three in a row
                row = False
        
        if(row == True):    # if three in a row return true
            Winner = play
            #print("1")
            return row

    for i in range(length):      # for each column
        col = True

        for j in range(len(board)):         # for each row
        
            play = board[0][i]         # get the first item in col to compare rest of col to

            if(play == None):
                col = False
                continue

            if(board[j][i] != play):   # see if three in a row downwards
                col = False
            
        if(col == True):    # if three in a row return true
            Winner = play
            #print("2")
            return col

    diag = True
    for i in range(length):      # for each row/col
        play = board[0][0]              # get left top corner item

        if(play == None):
            diag = False
            continue

        if(board[i][i] != play):        # make sure the diagonal items are same
            diag = False
    
    if(diag == True):       # if diagonal is 3 in row
        Winner = play
        #print("3")
        return diag
    
    
    j = length - 1
    diag = True
    for i in range(length):      # for each row/col
        play = board[0][length - 1]              # get left bottom corner item
        
        if(play == None):
            diag = False
            continue

        if(board[i][j] != play):        # make sure the diagonal items are same
            diag = False
        j -= 1
    
    if(diag == True):       # if diagonal is 3 in row
        Winner = play
        #print("4")
        return diag
    
    for i in board:
        for j in i:             # get number of empty spots
            #print(j)
            if(j == EMPTY):
                ecount += 1

    if(ecount == 0):        # if board is filled out
        Winner = EMPTY
        #print("5")
        return True
    
    Winner = None
    #print("6")
    return False        # if game still in play


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(Winner == EMPTY):
        return 0
    elif(Winner == X):
        return 1
    elif(Winner == O):
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if(terminal(board) == True):
        return None
    
    acts = actions(board)
    turn = player(board)        # get whos turn it is 

    moves = None
    max = -1000000000
    min = 1000000000

    for i in acts:
        res = result(board, i)

        if(turn == X):
            val = minVal(res)
            if(val > max):
                max = val
                moves = i

        elif(turn == O):
            val = maxVal(res)
            if(min > val):
                min = val
                moves = i
    
    return moves


def maxVal(board):
    val = -1000000000

    if(terminal(board) == True):
        return utility(board)
    
    moves = actions(board)
    for i in moves:
        val = max(val, minVal(result(board, i)))

    return val


def minVal(board):
    val = 1000000000

    if(terminal(board) == True):
        return utility(board)

    moves = actions(board)
    for i in moves:
        val = min(val, maxVal(result(board, i)))

    return val
