#Nicholas David Fay
#Tic Tak Toe Game
#CIS 407
#Eric W.

##################################
#imports
from collections import namedtuple
import sys

"""Global Variables"""

P1 = namedtuple('P1','name tile')
P1.name = "player1"
P2 = namedtuple('P2','name tile')
P2.name = "player2"
tile_list = ["X", "O"]
X = "X"
O = "O"

""" Functions """

def print_board(board_array, tiles):
	"""
	list (of lists) -> None
	This function is in chare of printing the board 
	after each move is made
	"""
	i = 0
	for row in board_array:
		print("{}   |{}| |{}| |{}|".format(i, row[0], row[1], row[2]))
		print("")
		i += 1
	print("")
	print("    0    1   2")
	print("Tiles on board: {}\n".format(tiles))
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

def init(tiles):
	"""
	None -> list (of lists)
	This function initializes players, as well as creates 
	the board for play, then returns the board
	"""
	print("------Tic Tak Toe Terminal------\nIn this version of Tic Tak Toe you must select 2 things to place a tile\n1) row number\n2) column number.\n Keep this in mind!")
	#Establish Player 1
	player1 = None
	while((player1 != O and player1 != X)):
		player1 = input("Player 1: Please choose either X or O:   ")
	#Based on player 1's entry establish player2
	if(player1 == O):
		player2 = X
	else:
		player2 = O
	P1.tile = player1
	P2.tile = player2
	print("Player 2, you are {}".format(player2))
	board = create_board()
	print_board(board, tiles)
	return board

def player_move(board, player):
	"""
	list (of lists), str -> None
	This function updates the board arrays with the 
	given players move selection
	"""
	print("\n{} it is your turn.".format(player.name))
	try:
		row = int(input("Enter the row you want to select (i.e 0-2): "))
		column = int(input("Enter the column you want to select (i.e 0-2): "))
	except:
		print("Error: Non number given. Try again")
		player_move
		return
	if(board[row][column] in tile_list):
		print("Error: Tile alrady on location row:{} col:{}".format(row, column))
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

def count_tiles_on_board(board):
	"""
	list -> int
	This function goes through the board 
	and determines how many tiles are currently placed on the board
	"""
	tiles = 0
	for row in board:
		for tile in row:
			if(tile == X or tile == O):
				tiles += 1
	return tiles

def tie(moves_made):
	"""
	None -> None
	This function determines if there are any
	possible moves left to make. If not then it is a tie
	"""
	if(9 == moves_made):
		print("TIE GAME!!")
		sys.exit()
	return

def main():
	"""
	None -> None
	This is the main function
	"""
	#initialize board
	tiles_on_board = 0
	board = init(0)
	#get the turn flag
	turn = P1.name
	#until the game is ended (There is a win: or a tie)
	while(True):
		#if its player ones turn
		if(turn == P1.name):
			#player one takes a move
			player_move(board, P1)
			#then switches to player two
			turn = P2.name
		else:
			#same as above just vice versa
			player_move(board, P2)
			turn = P1.name
		#get the tile count on the current board
		tiles_on_board = count_tiles_on_board(board)
		#print the board
		print_board(board, tiles_on_board)
		#check if a player has won the game
		player_won(board)
		#check to see if the two players have tied
		tie(tiles_on_board)
	return
		 
#call to main program
main()