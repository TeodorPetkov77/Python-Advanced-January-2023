matrix = [list(map(int, input().split())) for x in range(int(input()))]
primary_diagonal = sum([matrix[i][i] for i in range(len(matrix))])
secondary_diagonal = sum([matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))])

print(abs(primary_diagonal - secondary_diagonal))

# https://judge.softuni.org/Contests/Compete/Index/1835#1

# 2.	Diagonal Difference
# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
#
# On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the
# values for each column - N numbers separated by a single space. Print the absolute difference between the primary
# and the secondary diagonal sums. Examples Input	Output	Comments 3 11 2 4 4 5 6 10 8 -12	15	Primary diagonal:
# sum = 11 + 5 + (-12) = 4 Secondary diagonal: sum = 4 + 5 + 10 = 19 Difference: |4 - 19| = 15 4 -7 14 9 -20 3 4 9 21
# -14 6 8 44 30 9 7 -14	34

