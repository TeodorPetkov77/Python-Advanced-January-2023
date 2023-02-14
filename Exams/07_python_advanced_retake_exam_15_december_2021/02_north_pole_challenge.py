def move_player(decorations_f, gifts_f, cookies_f, current_row_f, current_col_f):
    for _ in range(steps):
        field[current_row_f][current_col_f] = "x"
        current_row_f += moves[direction][0]
        current_col_f += moves[direction][1]
        if current_row_f < 0:
            current_row_f = len(field) - 1
        elif current_row_f == len(field):
            current_row_f = 0
        if current_col_f < 0:
            current_col_f = len(field[current_row]) - 1
        elif current_col_f == len(field[current_row]):
            current_col_f = 0
        if field[current_row_f][current_col_f] == "D":
            decorations_f += 1
        elif field[current_row_f][current_col_f] == "G":
            gifts_f += 1
        elif field[current_row_f][current_col_f] == "C":
            cookies_f += 1
        field[current_row_f][current_col_f] = "Y"
        if sum([decorations_f, gifts_f, cookies_f]) == all_items:
            print("Merry Christmas!")
            break
    return decorations_f, gifts_f, cookies_f, current_row_f, current_col_f


def locate_player():
    for row_f in range(len(field)):
        for col_f in range(len(field[row_f])):
            if field[row_f][col_f] == "Y":
                return row_f, col_f


def count_all_items():
    all_items_f = len([x for row in field for x in row if x in ["D", "G", "C"]])
    return all_items_f


def create_field():
    rows_f = list(map(int, input().split(", ")))[0]
    return [input().split() for x in range(rows_f)]


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

decorations = 0
gifts = 0
cookies = 0

field = create_field()
current_row, current_col = locate_player()
all_items = count_all_items()


command = input()
while command != "End":
    command = command.split("-")
    direction = command[0]
    steps = int(command[1])
    decorations, gifts, cookies, current_row, current_col = \
        move_player(decorations, gifts, cookies, current_row, current_col)
    if all_items == sum([decorations, gifts, cookies]):
        break
    command = input()

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(' '.join(x)) for x in field]

# https://judge.softuni.org/Contests/Practice/Index/3306#1

# North Pole Challenge
#
# You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items scattered around the workshop.
# You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "Y"
# •	Christmas decorations are marked with the symbol "D"
# •	Gifts are marked with the symbol "G"
# •	Cookies are marked with the symbol "C"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given commands until you receive the command "End". The commands will be in the format "right/left/up/down-{steps}". You should move in the given direction with the given steps and collect all the items that come across. If you go out of the field, you should continue to traverse the field from the opposite side in the same direction. You should mark your path with "x". Your current position should always be marked with "Y".
# Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry Christmas!".
# Input
# •	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
# •	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
# •	On the following lines, you will receive commands in the format described above until you receive the command "End" or until you collect all items.
# Output
# •	On the first line, if you have collected all items, print:
# o	"Merry Christmas!"
# o	Otherwise, skip the line
# •	Next, print the number of collected items in the format:
# o	"You've collected:
# o	- {number_of_decoration} Christmas decorations
# o	- {number_of_gifts} Gifts
# o	- {number_of_cookies} Cookies"
# •	Finally, print the field, as shown in the examples.
# Constrains
# •	All the commands will be valid
# •	There will always be at least one item
# •	The dimensions of the matrix will be integers in the range [1, 20]
# •	The field will always have only one "Y"
# •	On the field, there will always be only the symbols shown above.
# Examples
# Input	Output
# 6, 5
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G
# left-3
# up-1
# left-2
# right-7
# up-1
# End	You've collected:
# - 2 Christmas decorations
# - 1 Gifts
# - 0 Cookies
# . . . . .
# C . . G .
# . C . . .
# G . Y C .
# x x x x x
# x . x x x
# 5, 6
# . . . . . .
# . . . . . .
# Y C D D . .
# . . . C . .
# . . . C . .
# right-3
# down-3	Merry Christmas!
# You've collected:
# - 2 Christmas decorations
# - 0 Gifts
# - 3 Cookies
# . . . . . .
# . . . . . .
# x x x x . .
# . . . x . .
# . . . Y . .
# 5, 2
# . .
# . .
# . Y
# . .
# . G
# up-1
# left-11
# down-10
# End	You've collected:
# - 0 Christmas decorations
# - 0 Gifts
# - 0 Cookies
# x .
# Y x
# x x
# x .
# x G