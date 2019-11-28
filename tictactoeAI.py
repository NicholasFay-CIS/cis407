#Nicholas David Fay
#AI Tic Tak Toe Game
#CIS 407
#Prof. Eric W.
##################################
##################################

"""imports"""
from collections import namedtuple
import random
import sys

"""Global Variables"""

P1 = namedtuple('P1','name tile')
P1.name = "player1"
P2 = namedtuple('P2','name tile')
P2.name = "player2"
tile_list = ["X", "O"]
X = "X"
O = "O"
FILLED_BOARD = 9

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
		i += 1
	print("")
	print("     0   1   2")
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

def copy_board(board):
	"""
	list(of lists) -> list(of lists)
	This function is in charge of copying the existing board
	for the A.I to use to calculate the best move.
	"""
	copy = []
	for row in board:
		row_list = []
		for item in row:
			row_list.append(item)
		copy.append(row_list)
	return copy

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

def player_move(board, player, AI):
	"""
	list (of lists), str, True -> None
	This function updates the board arrays with the 
	given players move selection
	"""
	if(AI == None):
		print("\n{} it is your turn.".format(player.name))
		try:
			row = int(input("Enter the row you want to select (i.e 0-2): "))
			column = int(input("Enter the column you want to select (i.e 0-2): "))
		except:
			print("Error: Non number given. Try again")
			player_move(board, player, None)
			return
	else:
		row = AI.row
		column = AI.col
	if(board[row][column] in tile_list):
		print("Error: Tile alrady on location row:{} col:{}".format(row, column))
		player_move(board, player, None)
		return
	board[row][column] = player.tile
	return

def check_if_space_is_free(board, row, col):
	"""
	list(of lists), int, int -> bool
	This checks to see if a given move is valid
	i.e if the space is empty on the board
	"""
	if(board[row][col] == "_"):
		return True
	return False

def make_random_move(board):
	"""
	list (of lists) -> list
	"""
	#list of possible moves row:i, col:j
	possible_moves = []
	#iterate through the row options
	for i in range(0,3):
		move = namedtuple('move','row col')
		#iterate through the column options
		for j in range(0,3):
			#if that move is a valid move
			is_free = check_if_space_is_free(board, i, j)
			if(is_free == True):
				move.row = i
				move.col = j
				possible_moves.append(move)
	move = random.choice(possible_moves)
	return move

def AI_move(board, player, opponent):
	"""
	list (of lists),str -> None
	This makes the A.I decision for the move that is best
	"""
	#check to see if the AI can win by placing a tile
	#iterate through the row possibilities
	for row in range(0,3):
		#iterate through the column possibilities
		for col in range(0,3):
			#make a copy of the actual board
			board_copy = copy_board(board)
			#using that copy check to see if the row:i col:j place is free
			is_free = check_if_space_is_free(board_copy, row, col)
			move = namedtuple('move','row col')
			move.row = row
			move.col = col
			#if it is free
			if(is_free == True):
				#if it is free make the move on the copy board
				player_move(board_copy, player, move)
				#if that moves determines a win for the AI 
				won = player_won(board_copy)
				if(won == 2):
					#Make that move and return
					player_move(board, player, move)
					return
	#check if opponent can place a tile and win
	#if so then place a tile there so they cannot
	for row in range(0,3):
		for col in range(0,3):
			board_copy = copy_board(board)
			is_free = check_if_space_is_free(board_copy, row, col)
			move = namedtuple('move','row col')
			move.row = row
			move.col = col
			if(is_free == True):
				player_move(board_copy, opponent, move)
				won = player_won(board_copy)
				if(won == 1):
					player_move(board, player, move)
					return
	#if the AI detects that a tile cannot stop the opponent from winning
	#as well as the AI winning, make a random move
	random_move = make_random_move(board)
	player_move(board,player, random_move)
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
					return 1
				else:
					return 2
				
	#check for a column win
	j = 0
	for j in range(3):
		if(board[0][j] == board[1][j] == board[2][j] and board[0][j] != '_'):
			if(board[0][j] == P1.tile):
				return 1
			else:
				return 2
			
	#check for a diagonal win
	if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_'):
		if(board[0][0] == P1.tile):
			return 1
		else:
			return 2

	#reverse diagonal
	if(board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_'):
		if(board[0][0] == P1.tile):
			return 1
		else:
			return 2
	return 0 

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
	if(FILLED_BOARD == moves_made):
		print("TIE GAME!! No free spaces left....")
		return 1
	return 0

def check_replay():
	"""
	None -> None
	This function checks to see if the player wants 
	to play again. Either against the AI or against another person
	"""
	again = input("Would you like to play again?:  ")
	while(again != "Yes" and again != "yes" and again != "No" and again != "no"):
		again = input("Would you like to play again?:  ")
	if(again == "yes" or again == "Yes"):
		main()
		return 
	else:
		sys.exit()

def main():
	"""
	None -> None
	This is the main function
	"""
	#initialize board
	tiles_on_board = 0
	board = init(0)

	AIGAME = input("Would you like to play against the computer Enter Yes or No:   ")
	while(AIGAME != "Yes" and AIGAME != "yes" and AIGAME != "No" and AIGAME != "no"):
		AIGAME = input("Would you like to play against the computer Enter Yes or No:   ")
	if(AIGAME == "yes" or AIGAME == "Yes"):
		AIGAME = True
	else:
		AIGAME = False
	#get the turn flag
	turn = P1.name
	#until the game is ended (There is a win: or a tie)
	while(True):
		#if its player ones turn
		if(turn == P1.name):
			#player one takes a move
			player_move(board, P1, None)
			#then switches to player two
			turn = P2.name
		else:
			#same as above just vice versa
			if(AIGAME == False):
				player_move(board, P2, None)
			else:
				AI_move(board, P2, P1)
			turn = P1.name
		#get the tile count on the current board
		tiles_on_board = count_tiles_on_board(board)
		#print the board
		print_board(board, tiles_on_board)
		#check if a player has won the game
		won = player_won(board)
		#check to see if the two players have tied
		tied = tie(tiles_on_board)
		#if the game was a tie or a win, check to see if they want to play again
		if(won > 0 or tied == 1):
			if(won == 2):
				print("---------GAME OVER:::{} Wins---------".format(P2.name))
			elif(won == 1):
				print("---------GAME OVER:::{} Wins---------".format(P1.name))
			else:
				print("---------GAME OVER:::Tie Game---------")
			check_replay()
	return
		 
#call to main program
if __name__ == "__main__":
	main()