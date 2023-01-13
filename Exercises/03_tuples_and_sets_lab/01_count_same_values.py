numbers = tuple(map(float, input().split()))
num_dict = {}

for num in numbers:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1

[print(f"{key} - {value} times") for key, value in num_dict.items()]

