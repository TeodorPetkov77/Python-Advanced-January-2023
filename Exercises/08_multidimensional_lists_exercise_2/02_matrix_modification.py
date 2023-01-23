rows = int(input())
matrix = [list(map(int, input().split())) for x in range(rows)]

command = input()
while command != "END":
    command = command.split()
    action, row, col, num = command[0], int(command[1]), \
                            int(command[2]), int(command[3])
    if row in range(len(matrix)) and col in range(len(matrix[0])):
        if action == "Add":
            matrix[row][col] += num
        elif action == "Subtract":
            matrix[row][col] -= num
    else:
        print("Invalid coordinates")
    command = input()

[(print(" ".join(list(map(str, matrix[i]))))) for i in range(len(matrix))]

# https://judge.softuni.org/Contests/Compete/Index/3194#1

# 2.	Matrix Modification
# Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.
# Examples
# Input	Output
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END	6 2 3
# 4 3 6
# 7 8 9
# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END	Invalid coordinates
# Invalid coordinates
# -41 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 101