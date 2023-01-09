expression = input()
parentheses = []


for index in range(len(expression)):
    if expression[index] == "(":
        parentheses.append(index)
    elif expression[index] == ")":
        print(expression[parentheses.pop():index + 1])

