usernames = [print(i) for i in {input() for x in range(int(input()))}]

# https://judge.softuni.org/Contests/Compete/Index/1833#0

# 1.	Unique Usernames
# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the collection on the console (the order does not matter):
# Examples
# Input	Output
# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234	George
# Peter
# NiceGuy1234
# 10
# Peter
# Maria
# Peter
# George
# Steve
# Maria
# Alex
# Peter
# Steve
# George	Peter
# Maria
# George
# Steve
# Alex