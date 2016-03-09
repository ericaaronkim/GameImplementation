import numpy as np
from numpy import *

#Toot and Otto game implementation for Gamescrafters

#defines the state object for the toot and otto game
#state keeps track of 4 things:
#the player whose turn it is, the board, and both players hands
#additional methods are helper methods for the neccessary solver functions and 
class State(object):
    """Base State class"""
    """0 for blank space, 1 for T, 2 for O"""
    toot = np.array([1,2,2,1])
    otto = np.array([2,1,1,2])
    boardDimensionHeight = 4
    boardDimensionLength = 6
    diagonalConnectionsAllowed = True

    def __init__(self, height = 4, length = 6):
        self.firstPlayerTurn = True
        self.boardDimensionHeight = height
        self.boardDimensionLength = length
        self.pieces = np.zeros((self.boardDimensionHeight,self.boardDimensionLength), dtype = int)
        self.hand1T = 6
        self.hand1O = 6
        self.hand2T = 6
        self.hand2O = 6

    #returns a new State object that is a copy of self
    def state_copy(self):
        copy = State()
        copy.firstPlayerTurn = self.firstPlayerTurn
        copy.pieces = self.pieces.copy()
        copy.hand1T = self.hand1T
        copy.hand1O = self.hand1O
        copy.hand2T = self.hand2T
        copy.hand2O = self.hand2O
        return copy

    #prints the current board with helpful indices on the left and the bottom
    def print_board(self):
        """ Currently just printing the numpy array. """
        for i in range(self.boardDimensionHeight):
            print self.pieces[i]

    def board_is_full(self):
        """ Make the entries True if it has a 0 and False if it has 1.
            Then sum up the booleans. If 0, then the board is full. """
        bool_pieces = (self.pieces == 0)
        return bool_pieces.sum() == 0

    #returns the score dictionary for the number of words, toot and otto
    def check_for_words(self):
        # first entry is number of toot's, second is otto's
        score = np.zeros(2, dtype = int)
        for x in range(self.boardDimensionHeight):
            for y in range(self.boardDimensionLength):
                if self.pieces[x,y] != 0:
                    word = None
                    if self.pieces[x,y] == 1:
                        word = State.toot
                        index = 0
                    elif self.pieces[x,y] == 2:
                        word = State.otto
                        index = 1
                    if word is None:
                        continue

                    if self.wordTest(x+1, y, word, 1, 0, 1):
                        score[index] += 1
                    if self.wordTest(x, y+1, word, 0, 1, 1):
                        score[index] += 1
                    if self.wordTest(x+1, y+1, word, 1, 1, 1):
                        score[index] += 1
                    if self.wordTest(x+1, y-1, word, 1, -1, 1):
                        score[index] += 1
        return score
            
    #helper function for checkForWords      
    def word_test(self, x, y, word, dx, dy, char_pos_in_word):
        if char_pos_in_word == 4:
            return True
        if x >= self.boardDimensionHeight or y >= self.boardDimensionLength or x < 0 or y < 0:
            return False
        if self.pieces[x,y] != word[char_pos_in_word]:
            return False
        return self.wordTest(x+dx, y+dy, word, dx, dy, char_pos_in_word+1)


#Implementation of the neccessary functions for the solver

#assumes that player1 goes for toot and player2 goes for otto

#assumes that if the score is tied, continue playing no matter how many matches
#takes in a state parameter which is a State object
#returns a string of the options win, loss, tie, draw, unkwown
def primitive(state):
    score = state.checkForWords()
    if score[1] >= 1 and score [0] >= 1:
        return 'tie'
    if score[0] >= 1:
        print("toot wins")
        if state.firstPlayerTurn:
            return 'win'
        return 'loss'
    elif score[0] >= 1:
        print("otto wins")
        if state.firstPlayerTurn:
            return 'loss'
        return 'win'
    if state.board_is_full():
        return 'tie'
    else:
        return 'unknown'

#action is defined as a tuple with the letter, and a board location
#example of an action: ("T", (2,3))

#takes in the parameter state, a State object
#returns a list of actions that are valid to be applied to the parameter state
def gen_moves(state):
    hand = np.append(state.hand2T,state.hand2O)
    if state.firstPlayerTurn:
        hand = np.append(state.hand1T,state.hand1O)

    possibleActions = []
    for y in range(State.boardDimensionLength):
        x = 0
        while x < State.boardDimensionHeight and state.pieces[3-x,y] != 0:
            x += 1
        if x < State.boardDimensionHeight:
            for i in range(2):
                if hand[i]>0:
                    possibleActions.append((i+1, (3-x,y)))
    return possibleActions

#returns the successor given by applying the parameter action to the parameter state
#the parameter action is a tuple with the letter, and a board location
#the parameter state is a State object
#must pass in a valid state and a valid action for that state, does not check
def make_move(state, action):
    successor = state.stateCopy()
    piece, loc = action

    successor.firstPlayerTurn = not state.firstPlayerTurn
    successor.pieces[loc] = piece
    if state.firstPlayerTurn and piece == 1:
        successor.hand1T -= 1
    elif state.firstPlayerTurn and piece == 0:
        successor.hand1O -= 1
    elif not state.firstPlayerTurn and piece == 0:
        successor.hand2T -= 1
    else:
        successor.hand2O -= 1
    return successor




init_pos = State()

#helpful prints for reference, understanding the code, and debugging
def example():
    print 'the initial position is the following:'
    init_pos.printBoard()
    print 'hand1T=' + str(init_pos.hand1T)
    print 'hand1O=' + str(init_pos.hand1O)
    print 'hand2T=' + str(init_pos.hand2T)
    print 'hand2O=' + str(init_pos.hand2O)
    print 'firstPlayerTurn=' + str(init_pos.firstPlayerTurn)
    possibleActions = gen_moves(init_pos)
    print 'these are the possible actions:'
    print possibleActions
    print 'primitive value:'
    print primitive(init_pos)

    s = make_move(init_pos, possibleActions[6])
    print 'this is the state after a move has been made'
    s.printBoard()
    print 'hand1T=' + str(s.hand1T)
    print 'hand1O=' + str(s.hand1O)
    print 'hand2T=' + str(s.hand2T)
    print 'hand2O=' + str(s.hand2O)
    print 'firstPlayerTurn=' + str(s.firstPlayerTurn)
    possibleActions = gen_moves(s)
    print 'New possible actions:'
    print possibleActions
    print 'primitive value:'
    print primitive(s)
