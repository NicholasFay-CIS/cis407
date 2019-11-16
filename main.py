#MAIN for TIC TACK TOE
#seting up repo
#MAIN for TIC TACK TOE
#seting up repo
import sys

def print_board(player_array):
	i = 0
	for row in player_array:
		print("{} {}".format(i, row))
		i += 1
	print("    0    1    2")
    
def create_board():
	"""
	None -> list (oflists)
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
	#Establish Player 1
	player1 = None
	while(player1 != "O" and player1 != "X"):
		player1 = input("Please choose either X or O:   ")
	#Based on player 1 establish player2
	if(player1 == "O"):
		player2 = "X"
	else:
		player2 = "O"
	print("Player 2, you are {}".format(player2))
	board = create_board()
	print_board(board)
	return board


def main():
	board = init()

main()