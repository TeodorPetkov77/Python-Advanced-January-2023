matrix = [list(map(int, input().split(", "))) for x in range(int(input()))]
matrix_flat = [num for row in matrix for num in row]
print(matrix_flat)

# https://judge.softuni.org/Contests/Practice/Index/1834#2

# 3.	Flattening Matrix Write a program that receives a matrix and prints the flattened version of it (a list with
# all the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4]. On the first
# line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for each column
# separated with a comma and a space ", ". Examples Input	Output 2 1, 2, 3 4, 5, 6	[1, 2, 3, 4, 5, 6] 3 10, 2,
# 21, 4 5, 20, 41, 9 6, 2, 4, 99	[10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]

