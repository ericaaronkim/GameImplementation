import ConnectionBoards

LOSS, WIN, TIE, DRAW, UNDECIDED = "LOSS", "WIN", "TIE", "DRAW", "UNDECIDED"

initialPosition = ConnectionBoards.ConnectionBoard(ConnectionBoards.ConnectionBoard.ticTacToe)

def primitive(board):
	answer = board.gameOver()
	if answer == ConnectionBoards.ConnectionBoard.tie:
		return TIE
	if answer:
		return WIN
	return LOSS

def generateMoves(board):
	return board.possibleActions()

def doMove(board, move):
	return board.generateSuccessor(move)
