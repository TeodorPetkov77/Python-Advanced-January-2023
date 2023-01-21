n = list(map(int, input().split(", ")))[0]
matrix = [list(map(int, input().split(", "))) for x in range(n)]
print(sum([sum(x) for x in matrix]))
print(matrix)

# https://judge.softuni.org/Contests/Practice/Index/1834#0

# 1.	Sum Matrix Elements Write a program that reads a matrix from the console and prints: •	The sum of all numbers
# in the matrix •	The matrix itself On the first line, you will receive the matrix sizes in the format "{rows},
# {columns}". On the next rows, you will get elements for each column separated by a comma and a space ", ". Examples
# Input	Output 3, 6 7, 1, 3, 3, 2, 1 1, 3, 9, 8, 5, 6 4, 6, 7, 9, 1, 0	76 [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6],
# [4, 6, 7, 9, 1, 0]]
