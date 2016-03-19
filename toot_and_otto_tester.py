from toot_and_otto import *

def tester(board):
	print_board(board)

	print check_for_words(board)

	print primitive(board)

###### CASE 1 ######
###### 1 toot ######
###### 0 otto ######

# [1 2 2 1 2 2]
# [1 1 1 1 2 2]
# [2 1 2 2 2 2]
# [2 1 1 1 1 1]

initial_position[1] = np.array([1,2,2,1,2,2])
initial_position[2] = np.array([1,1,1,1,2,2])
initial_position[3] = np.array([2,1,2,2,2,2])
initial_position[4] = np.array([2,1,1,1,1,1])

tester(initial_position)

###### CASE 2 ######
###### 2 toot ######
###### 0 otto ######

# [1 2 2 1 2 2]
# [2 1 1 1 2 2]
# [2 1 2 2 2 2]
# [1 1 1 1 1 1]

initial_position[1] = np.array([1,2,2,1,2,2])
initial_position[2] = np.array([2,1,1,1,2,2])
initial_position[3] = np.array([2,1,2,2,2,2])
initial_position[4] = np.array([1,1,1,1,1,1])

tester(initial_position)

###### CASE 3 ######
###### 3 toot ######
###### 0 otto ######

# [1 2 2 1 2 2]
# [2 2 1 1 1 2]
# [2 1 2 2 2 2]
# [1 1 1 1 1 1]

initial_position[1] = np.array([1,2,2,1,2,2])
initial_position[2] = np.array([2,2,1,1,1,2])
initial_position[3] = np.array([2,1,2,2,2,2])
initial_position[4] = np.array([1,1,1,1,1,1])

tester(initial_position)

###### CASE 4 ######
###### 3 toot ######
###### 1 otto ######

# [1 2 2 1 1 2]
# [2 2 1 1 1 2]
# [2 1 2 2 2 2]
# [1 1 1 1 1 2]

initial_position[1] = np.array([1,2,2,1,1,2])
initial_position[2] = np.array([2,2,1,1,1,2])
initial_position[3] = np.array([2,1,2,2,2,2])
initial_position[4] = np.array([1,1,1,1,1,2])

tester(initial_position)

###### CASE 5 ######
###### 3 toot ######
###### 3 otto ######

# [1 2 2 1 1 2]
# [2 2 1 1 2 2]
# [2 1 1 2 1 2]
# [1 1 1 2 2 1]

initial_position[1] = np.array([1,2,2,1,1,2])
initial_position[2] = np.array([2,2,1,1,2,2])
initial_position[3] = np.array([2,1,1,2,1,2])
initial_position[4] = np.array([1,1,1,2,2,1])

tester(initial_position)


###### Empty State ######
###### Testing gen_moves ######

# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]

# possible moves: (1, (3,0)), (2, (3,0)), (1, (3,1)), (2, (3,2))
#				  (1, (3,2)), (2, (3,2)), (1, (3,3)), (2, (3,3))
#				  (1, (3,4)), (2, (3,4)), (1, (3,5)), (2, (3,5))

initial_position[1] = np.array([0,0,0,0,0,0])
initial_position[2] = np.array([0,0,0,0,0,0])
initial_position[3] = np.array([0,0,0,0,0,0])
initial_position[4] = np.array([0,0,0,0,0,0])

tester(initial_position)
print gen_moves(initial_position)

















