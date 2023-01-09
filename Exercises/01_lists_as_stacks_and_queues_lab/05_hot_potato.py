from collections import deque

queue = deque(input().split())
n = int(input())

while len(queue) > 1:
    for i in range(n - 1):
        queue.append(queue.popleft())
    print(f"Removed {queue.popleft()}")
print(f"Last is {(queue.popleft())}")

# https://judge.softuni.org/Contests/Practice/Index/1830#4

# 5.	Hot Potato
# Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid. Every nth toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to the next kid. It continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by a single space. On the second line, you will receive the nth toss (integer) in which a child leaves the game.
# Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in the format "Last is {kid}".
# Examples
# Input	Output
# Tracy Emily Daniel
# 2	Removed Emily
# Removed Tracy
# Last is Daniel
# George Peter Michael William Thomas
# 10	Removed Thomas
# Removed Peter
# Removed Michael
# Removed George
# Last is William
# George Peter Michael William Thomas
# 1	Removed George
# Removed Peter
# Removed Michael
# Removed William
# Last is Thomas