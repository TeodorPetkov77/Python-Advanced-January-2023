sequence_1 = set(map(int, input().split()))
sequence_2 = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input().split()
    numbers = tuple(int(x) for x in command[2:len(command)])
    if command[0] == "Add":
        if command[1] == "First":
            [sequence_1.add(x) for x in numbers]
        elif command[1] == "Second":
            [sequence_2.add(x) for x in numbers]
    elif command[0] == "Remove":
        if command[1] == "First":
            [sequence_1.remove(x) for x in numbers if x in sequence_1]
        elif command[1] == "Second":
            [sequence_2.remove(x) for x in numbers if x in sequence_2]
    elif command[0] == "Check":
        print(sequence_2 < sequence_1 or sequence_1 < sequence_2)

print(", ".join([str(x) for x in sorted(sequence_1)]))
print(", ".join([str(x) for x in sorted(sequence_2)]))

# https://judge.softuni.org/Contests/Compete/Index/3159#0

# 1.	Numbers
# First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.
# Examples
# Input	Output
# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset	True
# 1, 2, 3, 4, 5, 6
# 1, 2, 3
# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5	False
# 2, 3, 4, 5, 6, 9
# 6