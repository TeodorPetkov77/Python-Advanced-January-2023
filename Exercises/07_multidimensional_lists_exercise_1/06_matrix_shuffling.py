rows, cols = list(map(int, input().split()))
matrix = [input().split() for x in range(rows)]

command = input()

while command != "END":
    command = command.split()
    if len(command) == 5 and "swap" in command and \
            max(int(command[1]), int(command[3])) < rows and \
            max(int(command[2]), int(command[4])) < cols:
        matrix[int(command[1])][int(command[2])], \
            matrix[int(command[3])][int(command[4])] = \
            matrix[int(command[3])][int(command[4])], \
            matrix[int(command[1])][int(command[2])]
        [print(" ".join(x)) for x in matrix]
    else:
        print("Invalid input!")
    command = input()

# https://judge.softuni.org/Contests/Compete/Index/1835#5

# 6.	Matrix Shuffling Write a program that reads a matrix from the console and performs certain operations with its
# elements. User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and (
# "row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword
# along with four valid coordinates (no more, no less), separated by a single space. •	If the command is valid,
# you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check
# if the operation was performed correctly). •	If the command is not valid (does not contain the keyword "swap",
# has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on
# to the following command. A negative value makes the coordinates not valid. Your program should finish when the
# command "END" is entered. Examples Input	Output 2 3 1 2 3 4 5 6 swap 0 0 1 1 swap 10 9 8 7 swap 0 1 1 0 END	5 2 3
# 4 1 6 Invalid input! 5 4 3 2 1 6 1 2 Hello World 0 0 0 1 swap 0 0 0 1 swap 0 1 0 0 END	Invalid input! World Hello
# Hello World
