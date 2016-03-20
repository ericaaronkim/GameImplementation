from collections import deque
import gamesman
game_module = __import__(sys.argv[1].replace('.py', ''))

#TODO: switch frontier to a deque so I can add to the front or back

def solve(board):
	exploredDict = dict()
	parents = dict() #has set of parents
	children = dict() #has set of children

	solve_up = Queue.Queue()
	primitives = []
	frontier = Queue.Queue()

	frontier.put(board)


	def addParentsToSolveUpQueue(state):
		for parent in parents[state]:
			solve_up.put(parent)

	while not frontier.empty():
		state = frontier.get()

		# if state not in exploredDict:
		primitive_val = primitive(state):
		if primitive_val != UNDECIDED:
			exploredDict[state] = primitive_val
			primitives.append(state)
		else:
			successors = []
			for move in possibleMoves(state):
				successorState = makeMove(state, move)
				if not parents.get(successorState):
					parents[successorState] = []
				else:
					parents[successorState].append(state)
				successors.append(successorState)
			children[state] = successors
			for successor in successors:
				frontier.put(successor)

	for primitive in primitives:
		addParentsToSolveUpQueue(primitive)

	while not solve_up.empty():
		state = solve_up.get()

		#TODO: need to make sure that state has all its children solved for Othello


		successorDict = dict()
		for successor in children[state]:
			if exploredDict[successor] not in successorDict:
				successorDict[exploredDict[successor]] = 1
			else: 
				successorDict[exploredDict[successor]] += 1



		if gamesman.LOSE in successorDict:
			exploredDict[state] = gamesman.WIN
			addParentsToQueue(state)
		elif successorDict.get(GameNode.WIN) >= len(children[state]):
			exploredDict[state] = gamesman.LOSE
			addParentsToQueue(state, frontier, exploredDict)






			# 	addParentsToQueue(state, frontier, exploredDict)
			# else:
			# 	successors = []
			# 	for move in possibleMoves(state):
			# 		successorState = makeMove(state, move)
			# 		successors.append(successorState)

			# 	allSuccessorsSolved = True
			# 	for successor in successors:
			# 		if successor not in exploredDict:
			# 			allSuccessorsSolved = False

			# 	if allSuccessorsSolved:
			# 		successorDict = dict()
			# 		for successor in successors:
			# 			if exploredDict[successor] not in successorDict:
			# 				successorDict[exploredDict[successor]] = 1
			# 			else: 
			# 				successorDict[exploredDict[successor]] += 1

			# 		if GameNode.LOSS in successorDict:
			# 			exploredDict[state] = GameNode.WIN
			# 			addParentsToQueue(state, frontier, exploredDict)
			# 		elif successorDict.get(GameNode.WIN) >= len(successors):
			# 			exploredDict[state] = GameNode.LOSS
			# 			addParentsToQueue(state, frontier, exploredDict)
			# 	else:
			# 		for successor in successors:
			# 			if successor not in exploredDict:
			# 				frontier.put(successor)

	# return exploredDict[board]