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