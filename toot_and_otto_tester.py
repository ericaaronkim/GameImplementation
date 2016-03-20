from toot_and_otto import *

def tester(state):
	state.printBoard()

	print state.checkForWords()

	print primitive(state)


###### CASE 1 ######
###### 1 toot ######
###### 0 otto ######

# [1 2 2 1 2 2]
# [1 1 1 1 2 2]
# [2 1 2 2 2 2]
# [2 1 1 1 1 1]

s = State()

s.pieces[0] = np.array([1,2,2,1,2,2])
s.pieces[1] = np.array([1,1,1,1,2,2])
s.pieces[2] = np.array([2,1,2,2,2,2])
s.pieces[3] = np.array([2,1,1,1,1,1])


###### CASE 2 ######
###### 2 toot ######
###### 0 otto ######

# [1 2 2 1 2 2]
# [2 1 1 1 2 2]
# [2 1 2 2 2 2]
# [1 1 1 1 1 1]

t = State()

t.pieces[0] = np.array([1,2,2,1,2,2])
t.pieces[1] = np.array([2,1,1,1,2,2])
t.pieces[2] = np.array([2,1,2,2,2,2])
t.pieces[3] = np.array([1,1,1,1,1,1])


###### CASE 3 ######
###### 3 toot ######
###### 0 otto ######

# [1 2 2 1 2 2]
# [2 2 1 1 1 2]
# [2 1 2 2 2 2]
# [1 1 1 1 1 1]

r = State()

r.pieces[0] = np.array([1,2,2,1,2,2])
r.pieces[1] = np.array([2,2,1,1,1,2])
r.pieces[2] = np.array([2,1,2,2,2,2])
r.pieces[3] = np.array([1,1,1,1,1,1])


###### CASE 4 ######
###### 3 toot ######
###### 1 otto ######

# [1 2 2 1 1 2]
# [2 2 1 1 1 2]
# [2 1 2 2 2 2]
# [1 1 1 1 1 2]

u = State()

u.pieces[0] = np.array([1,2,2,1,1,2])
u.pieces[1] = np.array([2,2,1,1,1,2])
u.pieces[2] = np.array([2,1,2,2,2,2])
u.pieces[3] = np.array([1,1,1,1,1,2])


###### CASE 5 ######
###### 3 toot ######
###### 3 otto ######

# [1 2 2 1 1 2]
# [2 2 1 1 2 2]
# [2 1 1 2 1 2]
# [1 1 1 2 2 1]

v = State()

v.pieces[0] = np.array([1,2,2,1,1,2])
v.pieces[1] = np.array([2,2,1,1,2,2])
v.pieces[2] = np.array([2,1,1,2,1,2])
v.pieces[3] = np.array([1,1,1,2,2,1])


###### partial board ######

# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [1 0 0 0 0 0]

# possible moves: (1, (2,0)), (2, (2,0)), (1, (3,1)), (2, (3,2))
#				  (1, (3,2)), (2, (3,2)), (1, (3,3)), (2, (3,3))
#				  (1, (3,4)), (2, (3,4)), (1, (3,5)), (2, (3,5))

p = State()

p.pieces[0] = np.array([0,0,0,0,0,0])
p.pieces[1] = np.array([0,0,0,0,0,0])
p.pieces[2] = np.array([0,0,0,0,0,0])
p.pieces[3] = np.array([1,2,2,1,0,0])




###### Empty State ######
w = State()

# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]
# [0 0 0 0 0 0]

# possible moves: (1, (3,0)), (2, (3,0)), (1, (3,1)), (2, (3,2))
#				  (1, (3,2)), (2, (3,2)), (1, (3,3)), (2, (3,3))
#				  (1, (3,4)), (2, (3,4)), (1, (3,5)), (2, (3,5))




















