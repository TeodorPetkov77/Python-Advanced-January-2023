def find_identical_squares(matrix_f, rows_f, cols_f):
    result = 0
    for row in range(rows_f - 1):
        for col in range(cols_f - 1):
            if matrix_f[row][col] == matrix_f[row][col + 1] == \
                    matrix_f[row + 1][col] == matrix_f[row + 1][col + 1]:
                result += 1
    print(result)


rows, cols = list(map(int, input().split()))
matrix = [input().split() for x in range(rows)]

find_identical_squares(matrix, rows, cols)

# https://judge.softuni.org/Contests/Compete/Index/1835#2

# 3.	2x2 Squares in Matrix Find the number of all 2x2 squares containing identical chars in a matrix. On the first
# line, you will receive the matrix's dimensions in the format "{rows} {columns}". On the following rows,
# you will receive characters separated by a single space. Print the number of all square matrices you have found.
# Examples Input	Output	Comments 3 4 A B B D E B B B I J B B	2	Two 2x2 squares of equal cells: A B B D	A B B
# D E B B B	E B B B I J B B	I J B B 2 2 a b c d	0	No 2x2 squares of equal cells exist. 5 4 A A B D A A B B I J B B C
# C C G C C K P	3	Three 2x2 squares of equal cells: A A B D  A A B D  A A B D A A B B  A A B B  A A B B I J B B  I J
# B B  I J B B C C C G  C C C G  C C C G C C K P  C C K P  C C K P
