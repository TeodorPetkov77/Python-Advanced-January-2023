from collections import deque

chocolates = deque(list(map(int, input().split(", "))))
cups = deque(list(map(int, input().split(", "))))
milkshakes = 0

while (chocolates and cups) and (milkshakes < 5):
    chocolate = chocolates[-1]
    cup = cups[0]
    if chocolate <= 0 or cup <= 0:
        if chocolate <= 0:
            chocolates.pop()
        if cup <= 0:
            cups.popleft()
        continue
    if chocolate == cup:
        cups.popleft()
        chocolates.pop()
        milkshakes += 1
    else:
        cups.append(cups.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join([str(x) for x in cups])}")
else:
    print("Milk: empty")

# https://judge.softuni.org/Contests/Compete/Index/3159#2

# 3.	Milkshakes
# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal, you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.
# Input
# •	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
# •	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
# •	On the first line, print:
# o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# o	Otherwise: "Not enough milkshakes."
# •	On the second line - print:
# o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# o	Otherwise: "Chocolate: empty"
# •	On the third line - print:
# o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# o	Otherwise: "Milk: empty"
# Constraints
# •	All given numbers will be valid integers in the range [-100 … 100].
# Examples
# Input	Output
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55	Great! You made all the chocolate milkshakes needed!
# Chocolate: 20
# Milk: 10, 55
# Comment
# 1) 26 == 26 -> You made chocolate milkshake. Remove both ingredients.
# 2) 60 == 60 -> You made chocolate milkshake. Remove both ingredients.
# 3) 22 == 22 -> You made chocolate milkshake. Remove both ingredients.
# 4) 17 == 17 -> You made chocolate milkshake. Remove both ingredients.
# 5) -5 is invalid, so it is removed before mixing.
# 6) 24 == 24 -> You made chocolate milkshake. Remove both ingredients. You made enough chocolate milkshakes. The program ends.
# Input	Output
# -10, -2, -30, 10
# -5	Not enough milkshakes.
# Chocolate: -10, -2, -30, 10
# Milk: empty
# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6	Great! You made all the chocolate milkshakes needed!
# Chocolate: empty
# Milk: 14, 6