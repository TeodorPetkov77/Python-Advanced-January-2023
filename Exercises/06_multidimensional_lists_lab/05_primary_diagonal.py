matrix = [[int(x) for x in input().split()] for i in range(int(input()))]
print(sum([matrix[x][x] for x in range(len(matrix[0]))]))

# https://judge.softuni.org/Contests/Practice/Index/1834#4

# 5.	Primary Diagonal Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from
# top left to bottom right). On the first line, you will receive an integer N – the size of a square matrix. The next
# N lines holds the values for each column - N numbers, separated by a single space.
#
# Examples
# Input	Output	Input	Output
# 3
# 11 2 4
# 4 5 6
# 10 8 -12	4	3
# 1 2 3
# 4 5 6
# 7 8 9	15
