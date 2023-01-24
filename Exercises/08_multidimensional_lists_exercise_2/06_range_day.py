def find_player(matrix_f):
    row_a, col_a = 0, 0
    for row_f in range(len(matrix_f)):
        for col_f in range(len(matrix_f)):
            if matrix_f[row_f][col_f] == "A":
                row_a, col_a = row_f, col_f
    return row_a, col_a


def move_player(matrix_f, row_p_f, col_p_f, skips_f, direction_f):
    move_row, move_col = row_p_f, col_p_f
    for _ in range(skips_f):
        move_row += moves[direction_f][0]
        move_col += moves[direction_f][1]
    if move_row in range(len(matrix_f)) and \
            move_col in range(len(matrix_f)):
        if matrix_f[move_row][move_col] != "x":
            matrix_f[row_p_f][col_p_f] = "."
            matrix_f[move_row][move_col] = "A"
            row_p_f = move_row
            col_p_f = move_col
    return matrix_f, row_p_f, col_p_f


def shoot(matrix_f, row_p_f, col_p_f, direction_f, kills_f):
    while True:
        row_p_f += moves[direction_f][0]
        col_p_f += moves[direction_f][1]
        if row_p_f in range(len(matrix_f)) and \
                col_p_f in range(len(matrix_f)):
            if matrix_f[row_p_f][col_p_f] == "x":
                matrix_f[row_p_f][col_p_f] = "."
                kills_f.append([row_p_f, col_p_f])
                break
        else:
            break
    return matrix_f, kills_f


matrix = [input().split() for x in range(5)]
total_targets = len([target for sublist in matrix for target in sublist
                     if target == "x"])
commands = int(input())

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row_p, col_p = find_player(matrix)
kills = []
targets_destroyed = False

for _ in range(commands):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == "shoot":
        matrix, kills = shoot(matrix, row_p, col_p, direction, kills)
    elif action == "move":
        skips = int(command[2])
        matrix, row_p, col_p = move_player(matrix, row_p, col_p, skips, direction)
    if total_targets == len(kills):
        targets_destroyed = True
        break

if targets_destroyed:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - len(kills)} targets left.")

[print(x) for x in kills]

# https://judge.softuni.org/Contests/Compete/Index/3194#5

# 6.	Range Day
# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
# •	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# •	5 lines representing the field (symbols, separated by a single space)
# •	N - count of commands
# •	On the following N lines - the commands in the format described above
# Output
# •	On the first line, print one of the following:
# o	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o	Otherwise:
#               	       "Training not completed! {count_left_targets} targets left."
# •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
# Constrains
# •	All the commands will be valid
# •	There will always be at least one target
# Examples
# Input	Output
# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1	Training not completed! 3 targets left.
# [4, 1]
# . . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right	Training completed! All 2 targets hit.
# [4, 1]
# [2, 2]
# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left	Training not completed! 1 targets left.
# [4, 1]