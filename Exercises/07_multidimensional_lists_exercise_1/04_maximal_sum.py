rows, cols = list(map(int, input().split()))
matrix = [[int(x) for x in input().split()] for n in range(rows)]

list_of_squares = []

for row in range(rows - 2):
    for col in range(cols - 2):
        temp = [
                matrix[row][col],
                matrix[row][col + 1],
                matrix[row][col + 2],
                matrix[row + 1][col],
                matrix[row + 1][col + 1],
                matrix[row + 1][col + 2],
                matrix[row + 2][col],
                matrix[row + 2][col + 1],
                matrix[row + 2][col + 2]
                ]
        list_of_squares.append(temp)

sum_values = [sum(x) for x in list_of_squares]
max_square = list_of_squares[sum_values.index(max(sum_values))]
print(f"Sum = {sum(max_square)}")
print(f"{max_square[0]} {max_square[1]} {max_square[2]}")
print(f"{max_square[3]} {max_square[4]} {max_square[5]}")
print(f"{max_square[6]} {max_square[7]} {max_square[8]}")

# https://judge.softuni.org/Contests/Compete/Index/1835#3

# 4.	Maximal Sum Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a
# maximum sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum. Input •	On
# the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1,
# 20] •	On the following lines, you will receive each row with its columns - integers, separated by a single space in
# the range [-20, 20] Output •	On the first line, print the maximum sum of the elements in the 3x3 square in the
# format "Sum = {sum}" •	On the following 3 lines, print each element of the found submatrix, separated by a single
# space Examples Input	Matrix	Output 4 5 1 5 5 2 4 2 1 4 14 3 3 7 11 2 8 4 8 12 16 4	 	Sum = 75 1 4 14 7 11 2 8
# 12 16 5 6 1 0 4 3 1 1 1 3 1 3 0 4 6 4 1 2 5 6 2 2 1 5 4 1 3 3 3 6 0 5		Sum = 34 2 5 6 5 4 1 6 0 5
