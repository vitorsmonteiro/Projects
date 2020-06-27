import sys


board = [[0, 0, 3, 0, 0, 7, 0, 0, 1],
    	[0, 6, 0, 0, 3, 0, 0, 7, 0],
    	[0, 0, 4, 0, 0, 0, 0, 0, 5],
    	[0, 0, 5, 0, 0, 0, 0, 0, 9],
    	[0, 8, 0, 0, 4, 0, 0, 6, 0],
    	[4, 0, 0, 0, 0, 0, 5, 0, 0],
    	[2, 0, 0, 0, 0, 0, 4, 0, 0],
    	[0, 7, 0, 0, 2, 0, 0, 1, 0],
    	[8, 0, 0, 6, 0, 0, 3, 0, 0]]

def show_board(board):
	num_cols = len(board)
	num_rows = len(board[0])
	for row in range(num_rows):
		if row % 3 == 0 and row != 0:
			print("-------------------")
		for col in range(num_cols):
			if col % 3 == 0 and col != 0:
				print("|", end = "")
			print(str(board[row][col]) + " ", end = "")
		print("")

def empty_position(board):
	num_cols = len(board)
	num_rows = len(board[0])
	for row in range(num_rows):
		for col in range(num_cols):
			if board[row][col] == 0:
				return (row, col)
	return None

def valid_number(board, num, pos):
	num_cols = len(board)
	num_rows = len(board[0])
	#Check row
	for col in range(num_cols):
		if num == board[pos[0]][col] and pos[1] != col:
			return False
	#Check column
	for row in range(num_rows):
		if num == board[row][pos[1]] and pos[0] != row:
			return False	
	#Check square
	x_square = pos[0] // 3
	y_square = pos[1] // 3
	for xsqr in range(x_square*3, x_square*3 + 3):
		for ysqr in range(y_square * 3, y_square*3 + 3):
			if board[xsqr][ysqr] == num and (xsqr,ysqr) != pos:
				return False

	return True

def solve(board):
    position = empty_position(board)
    if not position:
        return True
    else:
        row, col = position
    for num in range(1,10):
    	if valid_number(board, num, (row, col)):
        	board[row][col] = num
        	if solve(board):
        		return True
        	board[row][col] = 0

    return False
print("INITIAL GAME")
print("\n ----------------- \n")
show_board(board)
print("\n ----------------- \n")
print("SOLVED GAME")
print("\n ----------------- \n")
solve(board)
show_board(board)

