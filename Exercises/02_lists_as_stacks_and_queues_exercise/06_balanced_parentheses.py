parentheses = list(input())
work_list = []

for item in parentheses:
    work_list.append(item)
    if work_list:
        if item == "]" and work_list[len(work_list) - 2] == "[":
            work_list.pop()
            work_list.pop()
        elif item == ")" and work_list[len(work_list) - 2] == "(":
            work_list.pop()
            work_list.pop()
        elif item == "}" and work_list[len(work_list) - 2] == "{":
            work_list.pop()
            work_list.pop()

if work_list:
    print("NO")
else:
    print("YES")

# https://judge.softuni.org/Contests/Compete/Index/1831#5

# Balanced Parentheses
# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after the former. There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
# •	On a single line, you will receive a sequence of parentheses.
# Output
# •	For each test case, print on a new line "YES" if the parentheses are balanced.
# •	Otherwise, print "NO"
# Constraints
# •	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
# •	Each character of the sequence will be one of {, }, (, ), [, ]
# Examples
# Input	Output
# {[()]}	YES
# {[(])}	NO
# {{[[(())]]}}	YES