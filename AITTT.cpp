#include <iostream>
#include <string>
using namespace std;

class Board {
    private:
        char game_board[3][3];
        int Check_win() {
            int col = 0;
            int row = 0;
            for(int i = 0; i < 3; i++) {
                if(game_board[i][0] == game_board[i][1] && game_board[i][0] != '_') {
                    if(game_board[i][1] == game_board[i][2]) {
                        if(game_board[i][0] == 'X') {
                            return 0;
                        } else {
                            return 1;
                        }
                    }
                }

            }
            for(int i = 0; i < 3; i++) {
                if(game_board[0][i] == game_board[1][i] && game_board[0][i] != '_') {
                    if(game_board[1][i] == game_board[2][i]) {
                        if(game_board[0][i] == 'X') {
                            return 0;
                        } else {
                            return 1;
                        }
                    }
                }
            }
            if(game_board[0][0] == game_board[1][1] && game_board[1][1] == game_board[2][2] && game_board[0][0] != '_') {
                if(game_board[0][0] == 'X') {
                    return 0;
                } else {
                    return 1;
                }
            }
            if(game_board[0][2] == game_board[1][1] && game_board[1][1] == game_board[2][0] && game_board[0][2] != '_') {
                if(game_board[0][2] == 'X') {
                    return 0;
                } else {
                    return 1;
                }
            }
            return -1;

        }
   public:
        void make_board() {
            char empty_marker = '_';
            for(int i = 0; i < 3; i++) {
                for(int j = 0; j < 3; j++) {
                    game_board[i][j] = empty_marker;
                }
            }
        }
        void print_board() {
            int row = 0;
            cout << '\t' << 0 << '\t' << 1 << '\t' << 2 << endl << endl;
            for (int i = 0; i < 3; i++) {
                cout << row << '\t';
                row++;
                for(int j = 0; j < 3; j++) {
                    cout << game_board[i][j] << '\t';
                }
                cout << endl << endl;
            }
        }
        int Make_move(int move, char sign) {
            int x,y;
            if(move == 0) {
                cout << "player1 it is your move";
            } else {
                cout << "player2 it is your move";
            }
            cout << "Choose the row number: ";
            cin >> x;
            cout << "Choose the column number: ";
            cin >> y;
            if(x > 2 || x < 0) {
                cout << x << " is not a valid row number" << endl;
                Make_move(move, sign);
            } else if(y > 2 || y < 0) {
                cout << y << " is not a valid column number" << endl;
            }
            if(game_board[x][y] == '_') {
                game_board[x][y] = sign;
                return Check_win(); 
            }
            cout << "Row: " << x << " Column: " << y << " is not available" << endl;
            Make_move(move, sign);
        }
        
} board;


class Players {
    private:
        char sign1;
        char sign2;
        int move;
    public:
        string player1;
        string player2;
        void Get_players() {
            string player;
            sign1 = 'X';
            sign2 = 'O';
            cout << "Player1 (X): Input name:\t";
            cin >> player1;
            cout << "Player2 (O): Input name:\t";
            cin >> player2;
            move = 0;
            return;
        }
        void Print_Players() {
            string first_move;
            cout << "Player1:" << player1 << endl;
            cout << "Player2:" << player2 << endl;
            if(move == 0) {
                first_move = "player1's move.";
            } else {
                first_move = "player2's move.";
            }
            cout << first_move << endl;
            return;
        }
        int Get_player_move() {
            int temp_move = move;
            if(move == 0) {
                move++;
            } else {
                move--;
            }
            return temp_move;
        }
        char Get_player_sign(int player) {
            if(player == 0) {
                return sign1;
            } 
            return sign2;
        }
} play;

int main() {
    Board board;
    Players players;
    board.make_board();
    players.Get_players();
    players.Print_Players();
    board.print_board();
    int x = 0;
    while(x == 0) {
        int win;
        int move = players.Get_player_move();
        char sign = players.Get_player_sign(move);
        win = board.Make_move(move, sign);
        board.print_board();
        if(win == 0) {
            cout << "GAME OVER! " << players.player1 << " won" << endl;
            break;
        } else if(win == 1) {
            cout << "GAME OVER! " << players.player2 << " won" << endl;
        }
    }
    return 0;

}