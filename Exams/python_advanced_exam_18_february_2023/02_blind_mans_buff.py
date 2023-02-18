rows, cols = input().split()
rows, cols = int(rows), int(cols)
matrix = []
opponents = 0
moves = 0
player = [0, 0]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(rows):
    matrix.append(input().split())
    if "B" in matrix[row]:
        player[0], player[1] = row, matrix[row].index("B")


command = input()
while command != "Finish" and opponents < 3:
    next_row, next_col = player[0] + directions[command][0], \
                         player[1] + directions[command][1]
    if next_row in range(len(matrix)) and next_col in range(len(matrix[player[0]])):
        if matrix[next_row][next_col] == "O":
            command = input()
            continue
        elif matrix[next_row][next_col] == "P":
            opponents += 1
        moves += 1
        player[0], player[1] = next_row, next_col
    command = input()

print("Game over!")
print(f"Touched opponents: {opponents} Moves made: {moves}")

# https://judge.softuni.org/Contests/Compete/Index/3889#1

# 02. Blind Man’s Buff
#
# Blind man's buff is played in a spacious area, such as outdoors or in a large room, in which one player, is blindfolded and gropes around attempting to touch the other players without being able to see them…
# You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines, you will receive the rows of the playground, with M columns. You will be marked with the letter 'B', and placed in a random position. In random positions, furniture or other obstacles will be marked with the letter 'O'. The other players (opponents) will be marked with the letter 'P'. There will always be three other players participating in the game. All of the empty positions will be marked with '-'.
# Your goal is to touch as many players as possible during the game, without leaving the playground or stepping on an obstacle.
# On the next few lines, until you receive the command "Finish", you will receive a few lines with commands representing which direction you need to move. The possible directions are "up", " down", "right", and "left". If the direction leads you out of the field, you need to stay in position inside the field(do NOT make the move). If you have an obstacle, towards the direction, do NOT make the move and wait for the next command.
# You need to keep track of the count of touched opponents and the moves you’ve made.
# In case you step on a position marked with '-', increase the count of the moves made.
# When you receive a command with direction, you check the position you need to step on for an obstacle or opponent. If there is an opponent, you touch him and the position is marked with '-'(increase the count of the touched opponents and moves made), and this is your new position.
# The game is over when you manage to touch all other opponents or the given command is "Finish". A game report is printed on the Console:
# "Game over!"
# "Touched opponents: {count} Moves made: {count}"
#
# Input
# •	On the first line, you'll receive the dimensions of the playground in the format: "N M", where N is the number of rows, and M is the number of columns. They'll be separated by a single space (" ").
# •	On the next N lines, you will receive a string representing the respective row of the playground. The positions in every string will be separated by a single space (" ").
# •	On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right, left).
#  
# Output
# •	When the game is over, the following output should be printed on the Console:
# "Game over!"
# "Touched opponents: {count} Moves made: {count}"
# Constraints
# •	The playground size will be a 32-bit integer in the range [2 … 2 147 483 647].
# •	The playground will always have three opponents in it - 'P'.
# •	The obstacles on the playground will always be random count, and there will be cases without any obstacles.
# Examples
# Input	Output	Comments
# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish	Game over!
# Touched opponents: 1 Moves made: 3	       1. up	    2. up	3. left
# - - - O - P - O         - - - O - P - O        - - - O - P - O
# - P - O O - - -         - -P B O O - - -       - B - O O - - -
# - - B - - - O -          - - - - - - O -           - - - - - - O -
# - P- - O - - O          - -P- - O - - O         - P - - O - - O
# - - - O - - - -           - - - O - - - -           - - - O - - - -
#
#
#
#
# 4 4
# O B O -
# - P O P
# - - P -
# - - - -
# left
# right
# down
# right
# down
# right
# up
# right
# up
# down
# Finish	Game over!
# Touched opponents: 3 Moves made: 5	1. left
# Obstacle ahead - stays in the same position.
# 2. right
# Obstacle ahead - stays in the same position.
# 3. down
# O - O -
# - B O P
# - - P -
# - - - -
# Move made – increase moves counter
# Opponent touched – increase opponents touched counter
# 4. right
# Obstacle ahead - stays in the same position.
# 5. down
# O - O -
# - - O P
# - B P -
# - - - -
# Move made – increase moves counter
# 6. right
# O - O -
# - - O P
# - - B -
# - - - -
# Move made – increase moves counter
# Opponent touched – increase opponents touched counter
# 7. up
# Obstacle ahead - stays in the same position.
# 8. right
# O - O -
# - - O P
# - - - B
# - - - -
# Move made – increase moves counter
# 6. up
# O - O -
# - - O B
# - - - -
# - - - -
# Move made – increase moves counter
# Opponent touched – increase opponents touched counter
# This is the last opponent in the playground, so the game is over and the output is printed on the Console