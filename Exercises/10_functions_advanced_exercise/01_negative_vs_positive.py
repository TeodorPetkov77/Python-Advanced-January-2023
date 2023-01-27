def nvp(nums_list):
    negatives = sum([x for x in nums_list if x < 0])
    positives = sum([x for x in nums_list if x > 0])
    if abs(positives) < abs(negatives):
        return f"{negatives}\n{positives}\nThe negatives are stronger than the positives"
    else:
        return f"{negatives}\n{positives}\nThe positives are stronger than the negatives"


print(nvp(list(map(int, input().split()))))

# https://judge.softuni.org/Contests/Compete/Index/1839#0

# 1.	Negative vs Positive
# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. Find the total sum of the negatives and positives, and print the following:
# •	On the first line, print the sum of the negatives
# •	On the second line, print the sum of the positives
# •	On the third line:
# o	If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# o	If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.
# Example
# Input	Output
# 1 2 -3 -4 65 -98 12 57 -84	-189
# 137
# The negatives are stronger than the positives
# 1 2 3	0
# 6
# The positives are stronger than the negatives
