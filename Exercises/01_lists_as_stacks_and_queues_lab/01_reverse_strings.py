input_string = list(input())
result_string = []

for _ in range(len(input_string)):
    result_string.append(input_string.pop())

print("".join(result_string))

# https://judge.softuni.org/Contests/Practice/Index/1830#0

# 1.	Reverse Strings
# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console
# Examples
# Input	Output
# I Love Python	nohtyP evoL I
# Stacks and Queues	seueuQ dna skcatS

