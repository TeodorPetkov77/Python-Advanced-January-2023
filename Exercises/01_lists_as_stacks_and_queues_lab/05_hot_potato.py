from collections import deque

queue = deque(input().split())
n = int(input())
removed = ""

while len(queue) > 1:
    for i in range(n):
        removed = queue.popleft()
        if i < n - 1:
            queue.append(removed)
    print(f"Removed {removed}")
print(f"Last is {(queue.popleft())}")
