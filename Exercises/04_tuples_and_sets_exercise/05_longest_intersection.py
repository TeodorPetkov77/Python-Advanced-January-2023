n = int(input())
longest = ""

for _ in range(n):
    ranges = tuple(input().split("-"))
    first, second = ranges[0].split(",")
    third, fourth = ranges[1].split(",")
    intersection = {x for x in range(int(first), int(second) + 1)} & \
                   {x for x in range(int(third), int(fourth) + 1)}
    if len(intersection) > len(longest):
        longest = intersection

print(f"Longest intersection is {list(longest)} with length {len(longest)}")

# https://judge.softuni.org/Contests/Compete/Index/1833#4

# 5.	Longest Intersection
# Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
# Examples
# Input	Output	Comment
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10	Longest intersection is [6, 7, 8, 9, 10] with length 5	The intersection of [0-3] and [1-2] is [1-2] (length 2)
# The intersection of [2-10] and [3-5] is [3-5] (length 3)
# The intersection of [6-15] and [3-10] is [6-10] (length 5) - which is the longest
# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11	Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9