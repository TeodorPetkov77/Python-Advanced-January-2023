from collections import deque

elves = deque(list(map(int, input().split())))
materials = list(map(int, input().split()))
total_gifts = 0
total_energy = 0
turn = 0

while elves and materials:
    multiplier = 1
    turn += 1
    elf = elves.popleft()
    while elf < 5 and elves:
        elf = elves.popleft()
    if elf < 5:
        break
    if turn % 3 == 0:
        multiplier = 2
    if elf >= materials[-1] * multiplier:
        elf -= materials[-1] * multiplier
        total_energy += materials[-1] * multiplier
        if turn % 5 != 0:
            total_gifts += 1 * multiplier
            elf += 1
        materials.pop()
        elves.append(elf)
    else:
        elves.append(elf * 2)


print(f"Toys: {total_gifts}")
print(f"Energy: {total_energy}")
if elves:
    print(f"Elves left: {', '.join(map(str, [x for x in elves]))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, [x for x in materials]))}")

# https://judge.softuni.org/Contests/Practice/Index/3306#0

# Christmas Elves
#
# Everything in the Satna Claus' workshop was going well until, on one freezing Sunday, a dangerous storm destroyed almost all toys. Now Santa's elves fear they won't be able to meet their December deadline. It could be a disaster, and some children around the world may not get their Christmas toys. Luckily, you've come up with an idea, and you just need to write a program that manages your plan.
# The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.
# First, you will receive a sequence of integers representing each elf's energy. On the following line, you will be given another sequence of integers, each representing a number of materials in a box.
# Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.
# You are very clever and have immediately recognized the pros and cons of the work process - the first elf takes the last box of materials and tries to create the toy:
# •	Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy. His energy decreases by the used energy, and the toy goes straight to Santa's bag. Then, the elf eats a cookie reward which increases his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
# •	Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much energy as usual. If he has enough, he manages to create 2 toys. Then, his energy decreases; he eats a cookie reward and goes to the end of the line, similar to the first bullet.
# •	Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he just made it (if he made it). The toy is thrown away, and the elf doesn't get a cookie reward. However, his energy is already spent, and it needs to be added to the total elves' energy.
# o	If an elf creates 2 toys, but he is clumsy, he breaks them.
# •	If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy, the elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the upcoming boxes.
# Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he does NOT TAKE a box, but he takes a day off. Remove the elf from the collection.
# Stop crafting toys when you are out of materials or elves.
# Input
# •	The first line of input will represent each elf's energy - integers, separated by a single space
# •	On the second line, you will be given the number of materials in each box - integers, separated by a single space
# Output
# •	On the first line, print the number of created toys: "Toys: {total_number_of_toys}"
# •	On the second line, print the total used energy: "Energy: {total_used_energy}"
# •	On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
# o	"Elves left: {elf1}, {elf2}, … {elfN}"
# o	"Boxes left: {box1}, {box2}, … {boxN}"
# Constraints
# •	All the elves' values will be integers in the range [1, 100]
# •	All the boxes' values will be integers in the range [1, 100]
# Examples
# Input	Output	Comment
# 10 16 13 25
# 12 11 8	Toys: 3
# Energy: 31
# Elves left: 3, 6, 26, 14	1) The elf with energy 10 takes the box with 8 materials. He creates 1 gift and uses 8 units of energy. He eats a cookie and goes to the end of the line, which now looks like this: 16 13 25 3.
# 2) The elf with energy 16 takes the box with 11 materials. He creates 1 gift and uses 11 units of energy. Then, he eats a cookie and goes to the end of the line, which now looks like this: 13 25 3 6.
# 3) The elf with energy 13 takes the box with 12 materials. It is the third time an elf takes a box. The elf does not have the needed energy: 12 * 2, so he drinks a hot chocolate and goes to the end of the line: 25 3 6 26.
# 4) The elf with energy 25 takes the box with 12 materials. It is the fourth time an elf takes a box. He creates 1 gift and uses 12 units of energy. He eats a cookie and goes to the end of the line, which now looks like this: 3 6 26 14.
# No boxes are left, so the program ends. Print the desired text.
# 10 14 22 4 5
# 11 16 17 11 1 8
# 	Toys: 7
# Energy: 75
# Elves left: 10, 14
# 5 6 7
# 2 1 5 7 5 3	Toys: 3
# Energy: 20
# Boxes left: 2, 1