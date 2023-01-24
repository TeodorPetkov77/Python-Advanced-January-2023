def find_alice(matrix_f):
    row_a, col_a = 0, 0
    for row_f in range(len(matrix_f)):
        for col_f in range(len(matrix_f)):
            if matrix_f[row_f][col_f] == "A":
                row_a, col_a = row_f, col_f
    return row_a, col_a


def move_alice(matrix_f, alice_row_f, alice_col_f):
    tea_f = 0
    out_of_bounds = False
    while tea_f < 10 and out_of_bounds is False:
        move = input()
        matrix_f[alice_row_f][alice_col_f] = "*"
        move_row, move_col = alice_row_f + moves[move][0], \
                             alice_col_f + moves[move][1]
        if move_row in range(matrix_size) and move_col in range(matrix_size):
            if matrix_f[move_row][move_col].isnumeric():
                tea_f += int(matrix_f[move_row][move_col])
            elif matrix_f[move_row][move_col] == "R":
                out_of_bounds = True
            matrix_f[move_row][move_col] = "*"
        else:
            out_of_bounds = True
        alice_row_f, alice_col_f = move_row, move_col
    return matrix_f, tea_f


matrix_size = int(input())
matrix = [input().split() for x in range(matrix_size)]
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
alice_row, alice_col = find_alice(matrix)
matrix, tea = move_alice(matrix, alice_row, alice_col)

if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(" ".join(x)) for x in matrix]

# https://judge.softuni.org/Contests/Compete/Index/3194#4

# 5.	Alice in Wonderland
# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A".
# •	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# •	On the first line, you will be given the integer n – the size of the square matrix
# •	On the following n lines - matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will be given a move command
# Output
# •	On the first line:
# o	If Alice steps on the rabbit hole or she go out of the territory, print:
# "Alice didn't make it to the tea party."
# o	If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# •	On the following lines, print the matrix.
# Constraints
# •	Alice will always either go outside the Wonderland or collect 10 bags of tea
# •	All the commands will be valid
# •	All of the given numbers will be valid integers in the range [0, 10]
# Examples
# Input	Output
# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left	Alice didn't make it to the tea party.
# . * . . 1
# * * * . .
# 4 * . 1 .
# . . . 2 .
# . 3 . . .
# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right	She did it! She went to the party.
# * * . 1 1 . .
# * . . . 6 . 5
# * * . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2