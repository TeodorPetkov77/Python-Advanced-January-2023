def locate_white(matrix_f):
    for row_f in range(len(matrix_f)):
        for col_f in range(len(matrix_f)):
            if matrix[row_f][col_f] == "w":
                return row_f, col_f


def locate_black(matrix_f):
    for row_f in range(len(matrix_f)):
        for col_f in range(len(matrix_f)):
            if matrix[row_f][col_f] == "b":
                return row_f, col_f


def move_white(row_w_f, col_w_f, row_b_f, col_b_f, white_win_f, white_queen_f):
    if row_w_f == 0:
        white_queen_f = True
    elif (row_w_f - 1 == row_b_f and col_w_f - 1 == col_b_f) or \
            (row_w_f - 1 == row_b_f and col_w_f + 1 == col_b_f):
        white_win_f = True
    else:
        row_w_f -= 1
    return row_w_f, col_w_f, white_win_f, white_queen_f


def move_black(row_b_f, col_b_f, row_w_f, col_w_f, black_win_f, black_queen_f):
    if row_b_f == 7:
        black_queen_f = True
    elif (row_b_f + 1 == row_w_f and col_b_f - 1 == col_w_f) or \
            (row_b_f + 1 == row_w_f and col_b_f + 1 == col_w_f):
        black_win_f = True
    else:
        row_b_f += 1
    return row_b_f, col_b_f, black_win_f, black_queen_f


matrix = [input().split() for x in range(8)]
white_win = False
white_queen = False
black_win = False


black_queen = False


row_w, col_w = locate_white(matrix)
row_b, col_b = locate_black(matrix)


while True:
    row_w, col_w, white_win, white_queen = move_white(row_w, col_w, row_b, col_b, white_win, white_queen)
    if white_win:
        print(f"Game over! White win, capture on {chr(col_b + 97)}{8 - row_b}.")
        break
    elif white_queen:
        print(f"Game over! White pawn is promoted to a queen at {chr(col_w + 97)}{8 - row_w}.")
        break
    row_b, col_b, black_win, black_queen = move_black(row_b, col_b, row_w, col_w, black_win, black_queen)
    if black_win:
        print(f"Game over! Black win, capture on {chr(col_w + 97)}{8 - row_w}.")
        break
    elif black_queen:
        print(f"Game over! Black pawn is promoted to a queen at {chr(col_b + 97)}{8 - row_b}.")
        break

# https://judge.softuni.org/Contests/Practice/Index/3374#1

# Pawn Wars
#
# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
# •	Only move forward in a straight line:
# 	White (w) moves from the 1st rank to the 8th rank direction.
# 	Black (b) moves from 8th rank to the 1st rank direction.
# •	Can move only 1 square at a time.
# •	Can capture another pawn in from of them only diagonally:
#
# When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank), can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.
#
#
# Some rules apply when moving paws:
# •	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
# •	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
# Input
# •	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
# o	Empty positions are marked with "-".
# o	White pawn is marked with "w"
# o	Black pawn is marked with "b"
# Output
# Print either one of the following:
# •	If a pawn captures the other, print:
# o	"Game over! {White/Black} win, capture on {square}."
# •	If a pawn reaches the last rank, print:
# o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
# Constraints
# •	The input will always be valid.
# •	The matrix will always be 8x8.
# •	There will be no case where two pawns are placed on the same square.
# •	There will be no case where two pawns are placed on the same column.
# •	There will be no case where black/white will be placed on the last rank.
# Examples
# Input	Output	Comments
# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -	Game over! White pawn is promoted to a queen at b8.	We start by pushing the white pawn to b4, next, we push the black pawn to g7:
# - - - - - - - -
# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# Then white play b5, black play g6:
# - - - - - - - -
# - - - - - - - -
# - - - - - - b -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# …
# Capturing is not possible here, so after a few more moves, the white pawn is promoted to a queen on b8.
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - - - - - -
# - w - - - - - -
# - - - - - - - -	Game over! White win, capture on a3.	A white pawn always start first, so it must capture the black one on a3 in the first move:
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# w - - - - - - -
# - - - - - - - -
# - - - - - - - -