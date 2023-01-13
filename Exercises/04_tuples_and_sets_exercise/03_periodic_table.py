chemicals = set()
[[chemicals.add(x) for x in input().split()] for i in range(int(input()))]
[print(x) for x in chemicals]

# https://judge.softuni.org/Contests/Compete/Index/1833#2

# 3.	Periodic Table
# Write a program that keeps all the unique chemical elements. On the first line, you will be given a number n - the count of input lines that you will receive. On the following n lines, you will be receiving chemical compounds separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter):
# Examples
# Input	Output
# 4
# Ce O
# Mo O Ce
# Ee
# Mo	Ce
# Ee
# Mo
# O
# 3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne	Ch
# Ge
# Mo
# Nb
# Ne
# O
# Tc