rows = [int(x) for x in input().split(', ')][0]
matrix = [[int(x) for x in input().split()] for i in range(rows)]
for n in range(len(matrix[0])):
    print(sum([matrix[x][n] for x in range(len(matrix))]))

# https://judge.softuni.org/Contests/Practice/Index/1834#3

# 4.	Sum Matrix Columns Write a program that reads a matrix from the console and prints the sum for each column on
# separate lines. On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows,
# you will get elements for each column separated with a single space. Examples Input	Output	Input	Output 3,
# 6 7 1 3 3 2 1 1 3 9 8 5 6 4 6 7 9 1 0	12 10 19 20 8 7	3, 3 1 2 3 4 5 6 7 8 9	12 15 18
#
# Hints
# •	Read matrix sizes.
# •	On the next row lines, read the columns.
# •	Traverse the matrix and sum all elements in each column.
# •	Print the sum and continue with the other columns.
