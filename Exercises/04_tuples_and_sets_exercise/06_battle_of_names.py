n = int(input())
even_set = set()
odd_set = set()

for row in range(1, n + 1):
    result = sum([ord(x) for x in list(input())]) // row
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(even_set) == sum(odd_set):
    print(", ".join([str(x) for x in odd_set | even_set]))
elif sum(even_set) < sum(odd_set):
    print(", ".join([str(x) for x in odd_set - even_set]))
elif sum(even_set) > sum(odd_set):
    print(", ".join([str(x) for x in odd_set ^ even_set]))

# https://judge.softuni.org/Contests/Compete/Index/1833#5

# 6.	Battle of Names
# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ".
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set
# Examples
# Input	Output	Comment
# 4
# Pesho
# Stefan
# Stamat
# Gosho	304, 128, 206, 511	First name: Pesho. The sum of the ASCII values is: 80 + 101 + 115 + 104 + 111 = 511. Integer divide the sum to the current row (1): 511 / 1 = 511.
# Second name: Stefan. The sum of the ASCII values is: 83 + 116 + 101 + 102 + 97 + 110 = 609. Integer divide the sum to the current row (2): 609 / 2 = 304.
# Third name: Stamat. The sum of the ASCII values is: 83 + 116 + 97 + 109 + 97 + 116 = 618. Integer divide the sum to the current row (3): 618 / 3 = 206.
# Fourth name: Gosho. The sum of the ASCII values is: 71 + 111 + 115 + 104 + 111 = 512. Integer divide the sum to the current row (4): 512 / 4 = 128.
# The odd set: 511
# The even set: 304, 206, 128
# The sum of the even numbers is larger, so we print the symmetric-different values.
# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan	733, 101