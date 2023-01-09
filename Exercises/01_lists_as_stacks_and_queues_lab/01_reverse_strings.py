input_string = list(input())
result_string = []

for _ in range(len(input_string)):
    result_string.append(input_string.pop())

print("".join(result_string))