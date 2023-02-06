matrix = [list(input()) for x in range(int(input()))]
submarine_health = 3
battlecruisers = 3
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def locate_submarine(matrix_f, matrix_size_f):
    sub_row_f, sub_col_f = 0, 0
    for row in range(matrix_size_f):
        for col in range(matrix_size_f):
            if matrix_f[row][col] == "S":
                sub_row_f, sub_col_f = row, col
                break
    return sub_row_f, sub_col_f


def move_sub(matrix_f, sub_row_f, sub_col_f, submarine_health_f, battlecruisers_f, command_f):
    matrix_f[sub_row_f][sub_col_f] = "-"
    sub_row_f += directions[command_f][0]
    sub_col_f += directions[command_f][1]
    if matrix_f[sub_row_f][sub_col_f] == "*":
        submarine_health_f -= 1
    elif matrix_f[sub_row_f][sub_col_f] == "C":
        battlecruisers_f -= 1
    matrix_f[sub_row_f][sub_col_f] = "S"
    return matrix_f, sub_row_f, sub_col_f, submarine_health_f, battlecruisers_f


sub_row, sub_col = locate_submarine(matrix, len(matrix))

while submarine_health and battlecruisers:
    command = input()
    matrix, sub_row, sub_col, submarine_health, battlecruisers = \
        move_sub(matrix, sub_row, sub_col, submarine_health, battlecruisers, command)

if submarine_health:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
elif battlecruisers:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub_row}, {sub_col}]!")

[print("".join(x)) for x in matrix]

# https://judge.softuni.org/Contests/Practice/Index/3744#2

# 02. Navy Battle
# 1914, September 22 – German submarine U-9 sinks three unescorted British armored cruisers HMS Aboukir, HMS Hogue, and HMS Cressy in approximately one hour. Imagine that they had the technology to make themselves a navigational program for the submarine and you are chosen to implement the logic. Navigate U-9 through the battlefield, find and sink the British cruisers in the dark night, avoiding the floating mines all over the North Sea.
# You will be given an integer n for the size of the battlefield (square shape). On the next n lines, you will receive the rows of the battlefield. The submarine will start at a random position, marked with the letter 'S'. The submarine surveys the surrounding area through its periscope, so it has to climb up to periscope depth, where it might run across naval mines.
# When the submarine receives direction, it goes deep and moves one position toward the given direction. On each turn, you will be guiding the submarine and giving it the direction, in which it should move. The commands will be "up", "down", "left" and "right".
# When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
# •	If a position with '-' (dash) is reached, it means that the field is empty and the submarine awaits its next direction.
# •	If it runs across a naval mine ('*'), the submarine takes serious damage. When a mine is blown, the position of the mine will be marked with '-' (dash). U-9 can withstand two hits from naval mines.  The third time the submarine is hit by a mine, it disappears and the mission is failed. The battle is over and the following message should be printed on the Console: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
# •	If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed cruiser will be marked with '-' (dash).
# •	If this is the last (third) battle cruiser on the battlefield, the battle is over and the following message should be printed on the Console: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
# The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits mines three times).
# Input
# •	On the first line, you are given the integer n – the size of the matrix (wall).
# •	The next n lines hold the values for every row (NOT separated by anything).
# •	On each of the next lines you will get a direction command.
# Output
# •	If all battle cruisers are destroyed, print: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
# •	If U-9 is hit by a mine three times, print: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!".
# •	At the end, print the final state of the matrix (battlefield) with the last known U-9’s position on it.
# Constraints
# •	The size of the square matrix (battlefield) will be between [4…10].
# •	U-9’s starting position will always be marked with 'S'.
# •	There will be always three battle cruisers - fields marked with 'C'.
# •	There will be always enough mines on the battlefield to destroy the submarine.
# •	The commands given will direct the submarine only in the limits of the battlefield.
# Examples
# Input	Output
# 5
# *--*-
# -S-*C
# -*---
# -----
# -C-*C
# right
# down
# left
# up
# right
# right
# right
# down
# down
# down
# up
# left
# left
# left
# down	Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!
# *--*-
# -----
# -----
# -----
# -S-*-
#
# 5
# *--*-
# -S-*C
# -*---
# -----
# *C-*C
# right
# right
# up
# left
# left
# left	Mission failed, U-9 disappeared! Last known coordinates [0, 0]!
# S----
# ----C
# -*---
# -----
# *C-*C