def fill_the_box(*args):
    box_size = args[0] * args[1] * args[2]
    box_free_space = box_size - sum([x for x in list(args[3:args.index("Finish")])])
    if box_free_space > 0:
        return f"There is free space in the box. " \
               f"You could put {box_free_space} more cubes."
    else:
        return f"No more free space! You have {abs(box_free_space)} " \
               f"more cubes."

# https://judge.softuni.org/Contests/Compete/Index/1839#9

# 10.	*Fill the Box
# Write a function called fill_the_box that receives a different number of arguments representing:
# •	the height of a box
# •	the length of a box
# •	the width of a box
# •	n-times a different number of cubes with exact size 1 x 1 x 1
# •	a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
# •	If, at the end, there is free space left in the box, print:
# o	"There is free space in the box. You could put {free space in cubes} more cubes."
# •	If there is no free space in the box, print:
# o	"No more free space! You have {cubes left} more cubes."
# Examples
# Test Code	Output	Comment
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))	There is free space in the box. You could put 13 more cubes.	The size of the box: 2 * 8 * 2 = 32
# We put the cubes consistently. At the end there is more free space left.
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))	No more free space! You have 17 more cubes.	The size of the box: 5 * 5 * 2 = 50
# We put the cubes consistently. First, we put 40 cubes and there is free space left. Then we try to put 11 cubes, but there is only space for 10.
# Cubes left: 1 + 7 + 3 + 1 + 5 = 17
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))	There is free space in the box. You could put 960 more cubes.
