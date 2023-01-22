from collections import deque

size = int(input())
directions = deque(input().split())
matrix = [input().split() for x in range(size)]
player = [0, 0]
directions_dict = {"left": [0, -1],
                   "right": [0, 1],
                   "up": [-1, 0],
                   "down": [1, 0]}
coal_on_map = len([item for sublist in matrix for item in sublist if item == "c"])
collected_coal = 0
exit_reached = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            player = [row, col]
            break

while directions and coal_on_map and exit_reached is False:
    move = directions.popleft()
    move_row, move_col = [(player[0] + directions_dict[move][0]),
                          (player[1] + directions_dict[move][1])]
    if move_row in range(size) and move_col in range(size):
        item = matrix[move_row][move_col]
        if item == "c":
            collected_coal += 1
            coal_on_map -= 1
            matrix[move_row][move_col] = "*"
        elif item == "e":
            exit_reached = True
        player = [move_row, move_col]

if not coal_on_map:
    print(f"You collected all coal! ({(player[0])}, {player[1]})")
elif exit_reached:
    print(f"Game over! ({(player[0])}, {player[1]})")
else:
    print(f"{coal_on_map} pieces of coal left. ({(player[0])}, {player[1]})")

# https://judge.softuni.org/Contests/Compete/Index/1835#8

# 9.	*Miner
# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down".
# In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction. If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
# •	If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
# •	If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
# •	If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
# •	Field size - an integer number
# •	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
# •	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
# •	There are three types of output as mentioned above.
# Constraints
# •	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
# •	The field will always have only one "s"
# Examples
# Input	Output
# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *	Game over! (1, 3)
# 4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *	You collected all coal! (2, 3)
# 6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *	3 pieces of coal left. (5, 0)
