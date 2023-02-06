from collections import deque

mountain_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

climbed_peaks = []

daily_portions = list(map(int, input().split(", ")))
daily_staminas = deque(list(map(int, input().split(", "))))

for _ in range(7):
    portion = daily_portions.pop() if daily_portions else 0
    stamina = daily_staminas.popleft() if daily_staminas else 0
    total_portion_stamina = portion + stamina
    if total_portion_stamina >= mountain_peaks[0][1]:
        climbed_peaks.append(mountain_peaks[0][0])
        mountain_peaks.popleft()
        if not mountain_peaks:
            print("Alex did it! He climbed all top five Pirin "
                  "peaks in one week -> @FIVEinAWEEK")
            break
else:
    print("Alex failed! He has to organize his journey better next time "
          "-> @PIRINWINS")

if climbed_peaks:
    print("Conquered peaks:")
    [print(peak) for peak in climbed_peaks]


# https://judge.softuni.org/Contests/Practice/Index/3744#0

# 01. Climb the Peaks
# Alex is a vlogger and he wants to make videos of climbing the five highest peaks in Pirin mountain in just one week.  He will take his video set, a tent, and his backpack to the mountain. The backpack fits food portions for one week, exactly. His daily stamina is also limited. Your task is to trace his adventure and create a post for his profile @alaroundtheworld, at the end of the journey.
# You will have to keep information for all the conquered peaks if any.
# Every day, Alex will use one portion of his daily food supplies and will exhaust one of his daily stamina.
# First, you will be given a sequence of numbers, representing the quantities of the daily portions of food supplies in his backpack.
# Afterward, you will be given another sequence of numbers, representing the quantities of the daily stamina he will have at his disposal for the next seven days.
# You have to sum the quantity of the last daily food portion with the quantity of the first daily stamina. He will start climbing from the first peak in the table below to the last one.
# •	If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table below, it means that the peak is conquered. In this case, you should remove both quantities from the sequences and continue with the next ones towards the next peak.
# •	If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below, the peak remains unconquered. You should remove both quantities from the sequences. Alex will have to sleep in his tent. On the next day, he will try the same peak once again.
#
# Mountain Peaks	Difficulty level
# Vihren	80
# Kutelo	90
# Banski Suhodol	100
# Polezhan	60
# Kamenitza	70
#
# Alex will try to conquer as many peaks as he can in seven days. If he manages to climb all the peaks, the journey ends and the output is printed on the Console.
# Finally, print on the Console all the conquered peaks(in the order of climbing).
# Input
# •	On the first line, you will receive the food portions, separated by a comma and a single space (', ').
# •	On the second line, you will receive the stamina, separated by a comma and a single space (', ').
# Output
# •	On the first line – print whether Alex managed to reach his goal and climb all the peaks in his list:
# o	If he managed to conquer all: "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
# o	If he didn't manage to climb all of the peaks: "Alex failed! He has to organize his journey better next time -> @PIRINWINS"
# •	Then, in either case, you need to print all the conquered peaks (in the order of climbing) if any:
# "Conquered peaks:
# {peak1}
# {peak2}
# …
# {peakn}"
# o	If there are no concurred peaks, do NOT print this message.
# Constraints
# •	All of the given numbers will be valid integers in the range [0…100].
# Examples
# Input	Output	Comment
# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2	Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK
# Conquered peaks:
# Vihren
# Kutelo
# Banski Suhodol
# Polezhan
# Kamenitza	We start by taking the last daily portion quantity (40) and the first stamina quantity (40). Their sum is 40 + 40 = 80. After that, we check if the sum is equal to or greater than the first peak’s difficulty level. The sum of the food portion and the stamina for the day is equal to the peak’s difficulty level, so the peak is conquered. We remove both quantities from the sequences.
# We continue with the next peak, where we have also enough food and stamina to conquer it. After we conquer all five peaks, the program ends, and we print the final post on the Console. After that, we print all conquered peaks, every peak on a new line.
# 10, 20, 34, 26, 12, 10, 45
# 30, 28, 17, 17, 13, 10, 10	Alex failed! He has to organize his journey better next time -> @PIRINWINS
# 	We start by taking the last daily portion quantity (45) and the first stamina quantity (30). Their sum is 45 + 30 = 75. After that, we check if the sum is equal to or greater than the first peak’s difficulty level. The sum is not enough for the peak to be conquered. Alex will have to sleep in the tent. We remove both quantities from the sequences.
# On the next day, he will try the same peak once again, so he will need a sum of 80, from the food portion and the daily stamina. The sum is 10 + 28 = 40 and it is not enough. Alex will have to sleep in his tent once again. We remove both quantities from the sequences.
# He will not be able to climb any of the peaks, so we should print on the Console a message for an unsuccessful adventure. There won’t be any conquered peaks, so we will print only the status message on the Console.