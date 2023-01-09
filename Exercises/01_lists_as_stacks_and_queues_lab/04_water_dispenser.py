from collections import deque

water = int(input())
people = deque()
command = input()

while command != "Start":
    people.append(command)
    command = input()

command = input()
while command != "End":
    if "refill" in command:
        command = command.split()
        water += int(command[1])
    else:
        command = int(command)
        if water >= command:
            print(f"{people.popleft()} got water")
            water -= command
        else:
            print(f"{people.popleft()} must wait")
    command = input()
else:
    print(f"{water} liters left")

