def recursive_power(number, power):
    if power == 0:
        return 1

    if power == 1:
        return number

    return number * recursive_power(number, power - 1)

# https://judge.softuni.org/Contests/Practice/Index/1838#5

# 5.	Recursive Power
# Create a recursive function called recursive_power() which should receive a number and a power. Using recursion, return the result of number ** power. Submit only the function in the judge system.
# Examples
# Test Code	Output
# print(recursive_power(2, 10))	1024
# print(recursive_power(10, 100))	10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000