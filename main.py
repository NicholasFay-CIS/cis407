#MAIN for TIC TACK TOE
#seting up repo
def create_board(player_array):
	print("|--------|--------|--------|")
	print("|  {}    |  {}    |  {}    |".format(player_array[0], player_array[1], player_array[2]))
	print("|________|________|________|")
	print("|  {}    |  {}    |  {}    |".format(player_array[3], player_array[4], player_array[5]))
	print("|________|________|________|")
	print("|  {}    |  {}    |  {}    |".format(player_array[6], player_array[7], player_array[8]))
	print("|________|________|________|")




def main():
	#Establish Player 1
	player_array = [None] * 9
	player1 = raw_input("Please choose either X or O:   ")
	#Based on player 1 establish player2
	if(player1 == "O"):
		player2 = "X"
	else:
		player2 = "O"
	create_board(player_array)
