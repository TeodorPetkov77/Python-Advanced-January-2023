parking = set()
n = int(input())

for _ in range(n):
    direction, car = tuple(input().split(', '))
    if direction == "IN":
        parking.add(car)
    else:
        parking.remove(car)

if parking:
    [print(x) for x in parking]
else:
    print("Parking Lot is Empty")

# https://judge.softuni.org/Contests/Practice/Index/1832#3

# 4.	Parking Lot
# Write a program that:
# •	Records a car number for every car that enters the parking lot
# •	Removes a car number when the car leaves the parking lot
# On the first line, you will receive the number of commands - N. On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}". The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot. Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".
# Note: The order in which we print the result does not matter.
# Examples
# Input	Output
# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU	CA2844AA
# CA9999TT
# CA2822UU
# CA9876HH
# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA	Parking Lot is Empty