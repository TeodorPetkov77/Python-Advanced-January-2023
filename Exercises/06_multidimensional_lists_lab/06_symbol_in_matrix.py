matrix = [list(input()) for x in range(int(input()))]
look_for_symbol = input()
found_symbol = False

for row in range(len(matrix)):
    if found_symbol:
        break
    for col in range(len(matrix)):
        if matrix[row][col] == look_for_symbol:
            found_symbol = True
            print((row, col))
            break

if not found_symbol:
    print(f"{look_for_symbol} does not occur in the matrix")

# https://judge.softuni.org/Contests/Practice/Index/1834#5

# 6.	Symbol in Matrix Write a program that reads a number - N, representing the rows and columns of a square
# matrix. On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. After that,
# you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the
# format: "({row}, {col})". You should start searching from the top left. If there is no such symbol,
# print the message "{symbol} does not occur in the matrix". Examples Input	Output 3 ABC DEF X!@ !	(2, 1) 4 asdd xczc
# qwee qefw 4	4 does not occur in the matrix
