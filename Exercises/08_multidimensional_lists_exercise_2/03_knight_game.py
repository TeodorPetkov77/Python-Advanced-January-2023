matrix_size = int(input())
matrix = [list(input()) for x in range(matrix_size)]
moves = (
    (-1, -2),
    (-2, -1),
    (1, -2),
    (2, -1),
    (1, 2),
    (2, 1),
    (-1, 2),
    (-2, 1)
)

kills = 0
kills_dict = {}
killed_knights = 0
kills_possible = True

while kills_possible:
    kills_possible = False
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "K":
                kills = 0
                for move in moves:
                    move_row = row + move[0]
                    move_col = col + move[1]
                    if move_row in range(matrix_size) \
                            and move_col in range(matrix_size):
                        if matrix[move_row][move_col] == "K":
                            kills += 1
                            kills_possible = True
                if kills not in kills_dict:
                    kills_dict[kills] = []
                kills_dict[kills].append((row, col))
    killed_knights += 1 if kills_possible else 0
    row_to_kill = kills_dict[max(kills_dict)][0][0]
    col_to_kill = kills_dict[max(kills_dict)][0][1]
    matrix[row_to_kill][col_to_kill] = "0"
    kills_dict = {}

print(killed_knights)

# https://judge.softuni.org/Contests/Compete/Index/3194#2

# 3.	Knight Game
# Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack one another with one move are left.
# Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the same number of attacks, remove the top-left one.
# Input
# •	On the first line, you will receive integer N - the size of the board
# •	On the following N lines, you will receive strings with "K" and "0"
# Output
# •	Print a single integer with the number of knights that need to be removed.
# Constraints
# •	The size of the board will be 0 < N < 30
# •	Time limit: 0.3 sec. Memory limit: 16 MB
# Examples
# Input	Output
# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0	1
# 	2
# KK
# KK	0	8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK	12

