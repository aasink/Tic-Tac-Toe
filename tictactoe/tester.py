#from tictactoe import initial_state
import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

# down X win
testboard1 = [[X, O, X],
              [X, O, O], 
              [X, X, O]]

# full board tie
testboard2 = [[X, O, X], 
              [O, O, X], 
              [X, X, O]]

# R to L diag X win
testboard3 = [[X, O, X], 
              [O, X, X], 
              [X, O, O]]

# L to R diag X win
testboard4 = [[X, O, X], 
              [None, X, None], 
              [O, O, X]]

testboard5 = [[None, O, X], 
              [O, None, X], 
              [X, O, None]]

# accross X win
testboard6 = [[X, X, X], 
              [O, O, X], 
              [X, O, O]]

# O win
testboard7 = [[X, X, None], 
              [O, X, X], 
              [O, O, O]]
           
"""
board = ttt.initial_state()
print(testboard6)

nextplayer = ttt.player(testboard)
print(nextplayer)

done = ttt.terminal(testboard5)
print("done")
print(done)
print()

win = ttt.winner(testboard5)
print("win")
print(win)
print()

util = ttt.utility(testboard5)
print ("util")
print(util)
print() """

testboard8 = [[None, None, None], 
              [None, X, None], 
              [None, None, None]]

testboard9 = [[O, None, None], 
              [None, X, None], 
              [None, None, None]]

actions = ttt.actions(testboard9)
print(actions)