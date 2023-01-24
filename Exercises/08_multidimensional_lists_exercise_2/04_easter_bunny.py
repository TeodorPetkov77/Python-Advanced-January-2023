matrix_size = int(input())
matrix = [input().split() for x in range(matrix_size)]
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def find_bunny(matrix_f):
    rab_row_f, rab_col_f = 0, 0
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix_f[row][col] == "B":
                rab_row_f, rab_col_f = row, col
                break
    return rab_row_f, rab_col_f


def find_best_path(matrix_f, directions_f, rab_row_f, rab_col_f):
    most_eggs_f = 0
    best_direction_f = ""
    best_position_f = []
    for direction, coords in directions_f.items():
        eggs = 0
        position = []
        current_row = rab_row_f
        current_col = rab_col_f
        for _ in range(matrix_size):
            current_row += coords[0]
            current_col += coords[1]
            if 0 <= current_row < matrix_size and 0 <= current_col < matrix_size:
                if matrix_f[current_row][current_col] == "X":
                    break
                eggs += int(matrix_f[current_row][current_col])
                position.append([current_row, current_col])
            else:
                break
        if eggs >= most_eggs_f:
            most_eggs_f = eggs
            best_position_f = position
            best_direction_f = direction
    return best_direction_f, best_position_f, most_eggs_f


bunny_row, bunny_col = find_bunny(matrix)
best_direction, best_positions, most_eggs = find_best_path(matrix, directions,
                                                           bunny_row, bunny_col)

print(best_direction)
[print(x) for x in best_positions]
print(most_eggs)

# https://judge.softuni.org/Contests/Compete/Index/3194#3

# 4.	Easter Bunny
# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
# •	A number representing the size of the field
# •	The matrix representing the field (each position separated by a single space)
# Output
# •	The direction which should be considered as best (lowercase)
# •	The field positions from which we are collecting eggs as lists
# •	The total number of eggs collected
# Constraints
# •	There will NOT be two or more paths consisting of the same total amount of eggs.
# Examples
# Input	Output	Comment
# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0	right
# [3, 1]
# [3, 2]
# [3, 3]
# [3, 4]
# 87	The number of eggs if the bunny goes up is equal to 7. If he goes down = 9, there are no eggs on the left and 87 on the right. That's why the bunny should follow this direction (right) and collect the eggs provided there.
# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22	down
# [6, 2]
# [7, 2]
# 113