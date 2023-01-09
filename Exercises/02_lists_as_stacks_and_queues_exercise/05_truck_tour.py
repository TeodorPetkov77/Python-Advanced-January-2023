from collections import deque

stations = int(input())
stations_list = deque([list(map(int, input().split())) for x in range(stations)])

for n in range(stations):
    tank = 0
    for station in stations_list:
        tank += station[0]
        tank -= station[1]
        if tank < 0:
            stations_list.append(stations_list.popleft())
            break
    else:
        print(n)
        break
