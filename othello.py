import gamesman
import numpy as np

LOSS, WIN, TIE, DRAW, UNDECIDED = "LOSS", "WIN", "TIE", "DRAW", "UNDECIDED"

initial_position = np.zeros((9,8), dtype = int)
initial_position[4,] = np.array([0,0,0,1,2,0,0,0])
initial_position[5,] = np.array([0,0,0,2,1,0,0,0])
# top row contains: current player, first player (i.e. 1 is black, 2 is white)
initial_position[0,] = np.array([1,1,0,0,0,0,0,0])

def print_board(board):
	for i in range(1,9):
		print board[i]

def primitive(board):
	possible_actions = gen_moves(board)
	if possible_actions == []:
		if sum(sum(board == 1)) > sum(sum(board == 2)) and board[0,1] == 1:
			return WIN
		elif sum(sum(board == 1)) < sum(sum(board == 2)) and board[0,1] == 1:
			return LOSS
		else:
			return TIE
	return UNDECIDED

def gen_moves(board):
	return

def do_move(board, move):
	return





def example():
	return
