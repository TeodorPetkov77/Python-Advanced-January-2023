def bombs_away(matrix_f, row_f, col_f):
    for x in range(row_f - 1, row_f + 2):
        for y in range(col_f - 1, col_f + 2):
            if x == row_f and y == col_f:
                continue
            else:
                if x in range(len(matrix_f)) and y in range(len(matrix_f[x])) \
                        and matrix_f[x][y] > 0:
                    matrix_f[x][y] -= matrix_f[row_f][col_f]
    matrix_f[row_f][col_f] = 0
    return matrix_f


matrix = [list(map(int, input().split())) for x in range(int(input()))]
bombs = input().split()


for bomb in bombs:
    bomb_row, bomb_col = list(map(int, bomb.split(",")))
    if matrix[bomb_row][bomb_col] > 0:
        matrix = bombs_away(matrix, bomb_row, bomb_col)

alive_cells = [num for sublist in matrix for num in sublist if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(" ".join([str(x) for x in print_row])) for print_row in matrix]

# https://judge.softuni.org/Contests/Compete/Index/1835#7

# 8.	*Bombs You will be given a square matrix of integers, each integer separated by a single space, and each row
# will be on a new line. On the last line of input, you will receive indexes - coordinates of several cells separated
# by a single space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}". On those cells,
# there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes, it deals damage
# equal to its integer value to all the cells around it (in every direction and in all diagonals). One bomb can't
# explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below,
# it dies. Dead cells can't explode. You must print the count of all alive cells and their sum. Afterward,
# print the matrix with all its cells (including the dead ones). Input •	On the first line, you are given the
# integer N - the size of the square matrix. •	The following N lines hold each column's values - N numbers separated
# by a space. •	On the last line, you will receive the coordinates of the cells with the bombs in the format described
# above. Output •	On the first line, you need to print the count of all alive cells in the format: "Alive cells: {
# alive_cells}" •	On the second line, you need to print the sum of all alive cells in the format: "Sum: {
# sum_of_cells}" •	In the end, print the matrix. A space must separate the cells. Constraints •	The size of the
# matrix will be between [0…1000]. •	The bomb coordinates will always be in the matrix. •	The bomb's values will
# always be greater than 0. •	The integers of the matrix will be in the range [1…10000]. Examples Input	Output
# Comments 4 8 3 2 5 6 4 7 9 9 9 3 6 6 8 1 2 1,2 2,1 2,0	Alive cells: 3 Sum: 12 8 -4 -5 -2 -3 -3 0 2 0 0 -4 -1 -3
# -1 -1 2	1) The bomb with value 7 will explode and reduce the values of the cells around it. 2) The bomb with
# coordinates 2,1 and value 9 will explode and reduce its neighbor cells. 3) The bomb with coordinates 2,0 and value 9
# will explode. After that, you have to print the count of the alive cells - 3, and their sum - 12. Print the matrix
# after the explosions. 3 7 8 4 3 1 5 6 4 9 0,2 1,0 2,2	Alive cells: 3 Sum: 8 4 1 0 0 -3 -8 3 -8 0
#
