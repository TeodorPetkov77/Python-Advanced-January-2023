numbers = tuple(map(float, input().split()))
num_dict = {}

for num in numbers:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1

[print(f"{key} - {value} times") for key, value in num_dict.items()]

# https://judge.softuni.org/Contests/Practice/Index/1832#0

# 1.	Count Same Values
# You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". The number must be formatted to the first decimal point.
# Examples
# Input	Output
# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# 	-2.5 - 3 times
# 4.0 - 2 times
# 3.0 - 4 times
# -5.5 - 1 times
# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
# 	2.0 - 3 times
# 4.0 - 6 times
# 5.0 - 4 times
# 3.0 - 7 times