n = int(input())

unique_names = {input() for x in range(n)}
[print(x) for x in unique_names]

# https://judge.softuni.org/Contests/Practice/Index/1832#2

# 3.	Record Unique Names
# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.
# Examples
# Input	Output		Input	Output		Input	Output
# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey	Alan
# Joey
# Lee
# Joe
# Peter		7
# Lyle
# Bruce
# Alice
# Easton
# Shawn
# Alice
# Shawn	Easton
# Lyle
# Alice
# Bruce
# Shawn		6
# Adam
# Adam
# Adam
# Adam
# Adam
# Adam	Adam