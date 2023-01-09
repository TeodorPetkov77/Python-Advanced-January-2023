from collections import deque

queue = deque(input().split())
n = int(input())

while len(queue) > 1:
    for i in range(n - 1):
        queue.append(queue.popleft())
    print(f"Removed {queue.popleft()}")
print(f"Last is {(queue.popleft())}")
