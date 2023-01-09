numbers = input().split()
result = []
for num in range(len(numbers)):
    result.append(numbers.pop())
print(" ".join(result))