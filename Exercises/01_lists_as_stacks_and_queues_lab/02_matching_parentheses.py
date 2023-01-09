expression = input()
parentheses = []


for index in range(len(expression)):
    if expression[index] == "(":
        parentheses.append(index)
    elif expression[index] == ")":
        print(expression[parentheses.pop():index + 1])

# https://judge.softuni.org/Contests/Practice/Index/1830#1

# 2.	Matching Parentheses
# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.
# Examples
# Input	Output
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5	(2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))
# (2 + 3) - (2 + 3)	(2 + 3)
# (2 + 3)
# Hints
# Scan through the expression searching for parentheses:
# •	If you find an opening parenthesis, push the index into the stack.
# •	If you find a closing parenthesis, pop the topmost element from the stack. This is the index of the last opening parenthesis.
# •	Use the current index and the popped one to extract a set of parentheses.