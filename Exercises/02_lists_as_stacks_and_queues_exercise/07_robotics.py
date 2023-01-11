from collections import deque

available_robots = []

for bot in input().split(";"):
    name, work_time = bot.split("-")
    available_robots.append([name, int(work_time), int(work_time)])

hours, minutes, seconds = list(map(int, input().split(":")))
products = deque([])


def clock(hours_f, minutes_f, seconds_f):
    if seconds_f > 59:
        minutes_f += 1
        seconds_f = 0
    if minutes_f > 59:
        hours_f += 1
        minutes_f = 0
    if hours_f > 23:
        hours_f = 0
    return hours_f, minutes_f, seconds_f


def print_clock(hours_f, minutes_f, seconds_f):
    return f"[{hours_f:02d}:{minutes_f:02d}:{seconds_f:02d}]"


def robot_recharge(available: list):
    for robot_f in available:
        if robot_f[1] > robot_f[2]:
            robot_f[2] += 1
    return available


command = input()

while command != "End":
    products.append(command)
    command = input()

while products:
    seconds += 1
    hours, minutes, seconds = clock(hours, minutes, seconds)
    available_robots = robot_recharge(available_robots)
    for robot in available_robots:
        if robot[1] == robot[2]:
            robot[2] = 0
            print(f"{robot[0]} - {products.popleft()} "
                  f"{print_clock(hours, minutes, seconds)}")
            break
    else:
        products.append(products.popleft())

# https://judge.softuni.org/Contests/Compete/Index/1831#6

# 7.	*Robotics
# There is a robotics factory. The current project is assembly-line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free, it should take a product for processing and log its name, product, and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
# The robots are standing in the line in the order of their appearance.
# Input
# •	On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
# •	On the second line, you will get the starting time in the format "hh:mm:ss"
# •	Next, until the "End" command, you will get a product on each line.
# Output
# •	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
# Examples
# Input	Output
# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End	ROB - detail [08:00:01]
# SS2 - glass [08:00:02]
# NX8000 - wood [08:00:03]
# NX8000 - apple [08:00:06]
# ROB-8
# 7:59:59
# detail
# glass
# wood
# sock
# End	ROB - detail [08:00:00]
# ROB - wood [08:00:08]
# ROB - glass [08:00:16]
# ROB - sock [08:00:24]
