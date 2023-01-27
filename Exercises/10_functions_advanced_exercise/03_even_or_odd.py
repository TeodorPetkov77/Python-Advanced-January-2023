def even_odd(*args):
    num_list = list(args)
    command = num_list.pop()

    def even():
        return [x for x in num_list if x % 2 == 0]

    def odd():
        return [x for x in num_list if x % 2 != 0]

    if command == "even":
        return even()
    else:
        return odd()

# https://judge.softuni.org/Contests/Compete/Index/1839#2

# 3.	Even or Odd
# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.
# Submit only your function in the judge system.
# Examples
# Test Code	Output
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))	[2, 4, 6]
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))	[1, 3, 5, 7, 9]
