def find_santa(matrix_f):
    row_s_f, col_s_f = 0, 0
    for row_f in range(len(matrix_f)):
        for col_f in range(len(matrix_f)):
            if matrix_f[row_f][col_f] == "S":
                row_s_f, col_s_f = row_f, col_f
    return row_s_f, col_s_f


def move_santa(matrix_f, row_s_f, col_s_f, direction_f, presents_f, nice_kids_f):
    move_row, move_col = row_s_f, col_s_f
    move_row += moves[direction_f][0]
    move_col += moves[direction_f][1]
    if move_row in range(len(matrix_f)) and \
            move_col in range(len(matrix_f)):
        matrix_f[row_s_f][col_s_f] = "-"
        if matrix_f[move_row][move_col] == "V":
            presents_f -= 1
            nice_kids_f -= 1
        elif matrix_f[move_row][move_col] == "C":
            for direc in moves:
                check_row = move_row + moves[direc][0]
                check_col = move_col + moves[direc][1]
                if check_row in range(len(matrix_f)) and \
                        check_col in range(len(matrix_f)):
                    if matrix_f[check_row][check_col] == "V" or \
                            matrix_f[check_row][check_col] == "X":
                        nice_kids_f -= 1 if matrix_f[check_row][check_col] == "V" else 0
                        matrix_f[check_row][check_col] = "-"
                        presents_f -= 1
        row_s_f = move_row
        col_s_f = move_col
        matrix_f[row_s_f][col_s_f] = "S"
    return matrix_f, row_s_f, col_s_f, presents_f, nice_kids_f


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

presents = int(input())
matrix = [input().split() for x in range(int(input()))]
nice_kids = len([target for sublist in matrix for target in sublist
                 if target == "V"])
default_nice_kids = nice_kids
row_s, col_s = find_santa(matrix)

command = input()
while command != "Christmas morning":
    matrix, row_s, col_s, presents, nice_kids = \
        move_santa(matrix, row_s, col_s, command, presents, nice_kids)
    if presents:
        command = input()
    else:
        break

if not presents and nice_kids:
    print("Santa ran out of presents!")
[print(" ".join(x)) for x in matrix]
if not nice_kids:
    print(f"Good job, Santa! {default_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")

# https://judge.softuni.org/Contests/Compete/Index/3194#6

# 7.	Present Delivery
# The presents are ready, and Santa has to deliver them to the kids.
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V". There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive. If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
# Input
# •	On the first line, you are given the integer m - the count of presents
# •	On the second - integer n - the size of the neighborhood
# •	The following n lines hold the values for every row
# •	On each of the following lines you will get a command
# Output
# •	On the first line:
# o	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
# •	Next, print the matrix.
# •	In the end, print one of these messages:
# o	If he manages to give all the nice kids presents, print:
# "Good job, Santa! {count_nice_kids} happy nice kid/s."
# o	Otherwise, print:
# "No presents for {count nice kids} nice kid/s."
# Constraints
# •	The size of the square matrix will be between [2…10].
# •	Santa's position will be marked with 'S'.
# •	There will always be at least 1 nice kid.
# •	There won't be a case where the cookie is on the border of the matrix.
# Input	Output	Comments
# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning	- - - -
# - - - S
# - - - -
# X - - -
# Good job, Santa! 2 happy nice kid/s.	Santa has 5 presents. The size of the matrix is 4. After we receive the matrix, we start reading commands. The first one is "up". The "X" means there is a naughty kid, so Santa moves on without dropping any presents. Next, he reaches a nice kid and drops a present. The "down" command moves Santa to an empty cell. The last command before the "Christmas morning" message is "right". Again we have a nice kid. The count of nice kids reached 2, and we don't have any nice kids without presents left. So we print the appropriate message.
# 3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up	Santa ran out of presents!
# - - - -
# V - - -
# - - S -
# - - - -
# No presents for 1 nice kid/s.	The commands send Santa to a cell with a cookie, so all of the kids around him receive presents. He runs out of presents because we have 3 kids there and only 3 presents. The program ends, and we have 1 nice kid that hasn't received a present.