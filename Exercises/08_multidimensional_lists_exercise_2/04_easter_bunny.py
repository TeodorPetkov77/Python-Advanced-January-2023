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
    for dir, coors in directions_f.items():
        eggs = 0
        position = []
        current_row = rab_row_f
        current_col = rab_col_f
        for _ in range(matrix_size):
            current_row += coors[0]
            current_col += coors[1]
            if 0 <= current_row < matrix_size and 0 <= current_col < matrix_size:
                if matrix_f[current_row][current_col] == "X":
                    break
                if int(matrix_f[current_row][current_col]) >= 0:
                    eggs += int(matrix_f[current_row][current_col])
                    position.append([current_row, current_col])
            else:
                break
        if eggs > most_eggs_f:
            most_eggs_f = eggs
            best_position_f = position
            best_direction_f = dir
    return best_direction_f, best_position_f, most_eggs_f


bunny_row, bunny_col = find_bunny(matrix)
best_direction, best_positions, most_eggs = find_best_path(matrix, directions,
                                                           bunny_row, bunny_col)

print(best_direction)
[print(x) for x in best_positions]
print(most_eggs)