rows, cols = list(map(int, input().split(", ")))
matrix = [[int(x) for x in input().split(", ")] for n in range(rows)]

list_of_squares = []

for row in range(rows - 1):
    for col in range(cols - 1):
        temp = [matrix[row][col],
                matrix[row][col + 1],
                matrix[row + 1][col],
                matrix[row + 1][col + 1]]
        list_of_squares.append(temp)

sum_values = [sum(x) for x in list_of_squares]
max_square = list_of_squares[sum_values.index(max(sum_values))]
print(f"{max_square[0]} {max_square[1]} ")
print(f"{max_square[2]} {max_square[3]} ")
print(sum(max_square))

# https://judge.softuni.org/Contests/Practice/Index/1834#5

# 7.	Square with Maximum Sum Write a program that reads a matrix from the console and finds the 2x2 top-left
# submatrix with biggest sum of its values. On first line you will get matrix sizes in format "{rows}, {columns}".  On
# the next rows, you will get elements for each column, separated with a comma and a space ", ". You should print the
# found submatrix and the sum of its elements, as shown in the examples. Examples Input	Output 3, 6 7, 1, 3, 3, 2,
# 1 1, 3, 9, 8, 5, 6 4, 6, 7, 9, 1, 0	9 8 7 9 33 2, 4 10, 11, 12, 13 14, 15, 16, 17	12 13 16 17 58 Hints •	Be
# aware of IndexError •	If you find more than one max square, print the top-left one
