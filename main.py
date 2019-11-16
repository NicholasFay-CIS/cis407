#Nicholas David Fay
#Tic Tak Toe Game
#CIS 407

#imports
from collections import namedtuple
import sys

"""Global Variables"""

P1 = namedtuple('P1','name tile')
P1.name = "player1"
P2 = namedtuple('P2','name tile')
P2.name = "player2"
tile_list = ["X", "O"]

""" Functions """

def print_board(board_array):
	"""
	list (of lists) -> None
	This function is in chare of printing the board 
	after each move is made
	"""
	i = 0
	for row in board_array:
		print("{} {}".format(i, row))
		i += 1
	print("    0    1    2")
	return
    
def create_board():
	"""
	None -> list (oflists)
	This function initializes the board to empty
	where empty slot is denoted as '_'
	"""
	board = []
	row1 = ["_"] * 3
	board.append(row1)
	row2 = ["_"] * 3
	board.append(row2)
	row3 = ["_"] * 3
	board.append(row3)
	return board

def init():
	"""
	None -> list (of lists)
	This function initializes players, as well as creates 
	the board for play, then returns the board
	"""
	print("------Tic Tak Toe Terminal------\nIn this version of Tic Tak Toe you must select 2 things to place a tile\n1) row number\n2) column number.\n Keep this in mind!")
	#Establish Player 1
	player1 = None
	while(player1 != "O" and player1 != "X"):
		player1 = input("Player 1: Please choose either X or O:   ")
	#Based on player 1 establish player2
	if(player1 == "O"):
		player2 = "X"
	else:
		player2 = "O"
	P1.tile = player1
	P2.tile = player2
	print("Player 2, you are {}".format(player2))
	board = create_board()
	print_board(board)
	return board

def player_move(board, player):
	"""
	list (of lists), str -> None
	This function updates the board arrays with the 
	given players move selection
	"""
	print("{} it is your turn.".format(player.name))
	row = int(input("Enter the row you want to select (i.e 0-2): "))
	column = int(input("Enter the column you want to select (i.e 0-2): "))
	if(board[row][column] in tile_list):
		print("Error: A tile already exists there...try again")
		player_move(board, player)
		return
	board[row][column] = player.tile
	return

def player_won(board):
	"""
	list (oflists) -> None
	This function checks to tell if a player has won
	checks rows
	checks columns 
	checks diagonal
	"""
	#check if 3 in row
	for row in board:
		if(row[0] == row[1] and row[0] != '_'):
			if(row[1] == row[2]):
				if(row[0] == P1.tile):
					print("GAME OVER: Row Win by {}".format(P1.name))
				else:
					print("GAME OVER: Row Win by {}".format(P2.name))
				sys.exit()
	#check for a column win
	j = 0
	for j in range(3):
		if(board[0][j] == board[1][j] == board[2][j] and board[0][j] != '_'):
			if(board[0][j] == P1.tile):
				print("GAME OVER: Column Win by {}".format(P1.name))
			else:
				print("GAME OVER: Column Win by {}".format(P2.name))
			sys.exit()
	#check for a diagonal win
	if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_'):
		if(board[0][0] == P1.tile):
			print("GAME OVER: Diagonal Win by {}".format(P1.name))
		else:
			print("GAME OVER: Diagonal Win by {}".format(P2.name))
		sys.exit()

	#reverse diagonal
	if(board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_'):
		if(board[0][0] == P1.tile):
			print("GAME OVER: Diagonal Win by {}".format(P1.name))
		else:
			print("GAME OVER: Diagonal Win by {}".format(P2.name))
		sys.exit()
	return

def main():
	"""
	None -> None
	This is the main function
	"""
	board = init()
	turn = P1.name
	while(True):
		if(turn == P1.name):
			player_move(board, P1)
			turn = P2.name
		else:
			player_move(board, P2)
			turn = P1.name
		print_board(board)
		player_won(board)

main()