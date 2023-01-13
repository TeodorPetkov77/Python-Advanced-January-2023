text = tuple(input())
[print(f"{x}: {text.count(x)} time/s") for x in sorted(set(text))]

# https://judge.softuni.org/Contests/Compete/Index/1833#3

# 4.	Count Symbols
# Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order.
# Examples
# Input	Output	Input	Output
# SoftUni rocks	 : 1 time/s
# S: 1 time/s
# U: 1 time/s
# c: 1 time/s
# f: 1 time/s
# i: 1 time/s
# k: 1 time/s
# n: 1 time/s
# o: 2 time/s
# r: 1 time/s
# s: 1 time/s
# t: 1 time/s	Why do you like Python?	: 4 time/s
# ?: 1 time/s
# P: 1 time/s
# W: 1 time/s
# d: 1 time/s
# e: 1 time/s
# h: 2 time/s
# i: 1 time/s
# k: 1 time/s
# l: 1 time/s
# n: 1 time/s
# o: 3 time/s
# t: 1 time/s
# u: 1 time/s
# y: 3 time/s