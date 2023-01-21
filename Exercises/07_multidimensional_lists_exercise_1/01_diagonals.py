matrix = [list(map(int, input().split(", "))) for x in range(int(input()))]
primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. "
      f"Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. "
      f"Sum: {sum(secondary_diagonal)}")

# https://judge.softuni.org/Contests/Compete/Index/1835#0

# 1.	Diagonals Using a nested list comprehension, write a program that reads rows of a square matrix and its
# elements, separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum
# in the format: "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary} Secondary diagonal: {
# element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}". Examples Input	Output 3 1, 2, 3 4, 5, 6 7, 8,
# 9	Primary diagonal: 1, 5, 9. Sum: 15 Secondary diagonal: 3, 5, 7. Sum: 15
