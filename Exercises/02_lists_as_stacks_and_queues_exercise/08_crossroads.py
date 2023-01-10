from collections import deque

green_time_default = int(input())
windows_time_default = int(input())

car_queue = deque([])
crossroads = []
passed_cars = []

crash_happened = False

while True:
    if crash_happened:
        break
    command = input()
    if command == "END":
        break
    if command == "green":
        green_time = green_time_default
        windows_time = windows_time_default
        for car in range(len(car_queue)):
            if green_time > 0:
                crossroads = car_queue.popleft()
                result = ""
                for char in crossroads:
                    if green_time > 0:
                        green_time -= 1
                        result += char
                    else:
                        if windows_time == 0:
                            print("A crash happened!")
                            print(f"{crossroads} was hit at {char}.")
                            crash_happened = True
                            break
                        windows_time -= 1
                        result += char
                else:
                    passed_cars.append(result)
    car_queue.append(command)

if not crash_happened:
    print("Everyone is safe.")
    print(f"{len(passed_cars)} total cars passed the crossroads.")

# https://judge.softuni.org/Contests/Compete/Index/1831#7

# 8.	*Crossroads
# The super-spy action hero Sam has finally found some time to go on a holiday. He is taking his wife somewhere nice, and they're going to have a really good time, but first, they have to get there. Even on his holiday trip, Sam is still going to run into some problems, and the first one is getting to the airport. Right now, he is stuck in a traffic jam at a crossroads where a lot of accidents happen.
# Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the crossroads safely.
# Sam is on a single lane of cars that queue until the light goes green. When it does, they start passing one by one on a flashing green light and during the free window before the intersecting road's light goes green. For each second, only one part of a car (a single character) passes the crossroad. If a car is still in the middle of the crossroads when the free window ends, it will get hit at the first character that is still in the crossroads.
# Input
# •	On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
# •	On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
# •	On the following lines, until you receive the "END" command, you will receive one of two things:
# 	A car - a string containing the model of the car, or
# 	The command "green" that indicates the start of a green light cycle
# A green light cycle goes as follows:
# •	During the green light, cars will enter and exit the crossroads one by one
# •	During the free window, cars will only exit the crossroads
# Output
# •	If a crash happens, end the program and print:
# "A crash happened!"
# "{car} was hit at {character_hit}."
# •	If everything goes smoothly and you receive an "END" command, print:
# "Everyone is safe."
# "{total_cars_passed} total cars passed the crossroads."
# Constraints
# •	The input will be within the constraints specified above and will always be valid. There is no need to check it explicitly.
# Examples
# Input	Output	Comments
# 10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END	Everyone is safe.
# 3 total cars passed the crossroads.	During the first green light (10 seconds), the Mercedes (8) passes safely.
# During the second green light, the Mercedes (8) passes safely, and there are 2 seconds left.
# The BMW enters the crossroads, and when the green light ends, it still has 1 part inside ('W') but has 5 seconds to leave and passes successfully.
# The Skoda never entered the crossroads, so 3 cars passed successfully.
# 9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END	A crash happened!
# Hummer was hit at e.
# 	Mercedes (8) passes successfully, and Hummer (6) enters the crossroads, but only the 'H' passes during the green light. There are 3 seconds of a free window, so "umm" passes, and the Hummer gets hit at 'e', and the program ends with a crash.