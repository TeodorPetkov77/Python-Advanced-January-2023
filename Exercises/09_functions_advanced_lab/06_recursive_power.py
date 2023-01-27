import functools


def operate(operator, *args):

    def add():
        result = sum(args)
        return result

    def subtract():
        result = functools.reduce(lambda a, b: a - b, args)
        return result

    def multiply():
        result = functools.reduce(lambda a, b: a * b, args)
        return result

    def divide():
        result = functools.reduce(lambda a, b: a / b, args)
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()

# https://judge.softuni.org/Contests/Practice/Index/1838#4

# 6.	Operate
# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers (integers) as additional arguments (*args). The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division
# Examples
# Test Code	Output	Comment
# print(operate("+", 1, 2, 3))	6	1 + 2 + 3 = 6
# print(operate("*", 3, 4))	12	3 * 4 = 12