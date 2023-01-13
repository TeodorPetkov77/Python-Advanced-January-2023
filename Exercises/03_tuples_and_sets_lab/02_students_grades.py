n = int(input())
students = {}

for _ in range(n):
    student, grade = tuple(input().split())
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for key, value in students.items():
    print(key, end=" -> ")
    [print(f"{x:.2f}", end=" ") for x in value]
    print(f"(avg: {sum(value) / len(value):.2f})")

# https://judge.softuni.org/Contests/Practice/Index/1832#1

# 2.	Students' Grades
# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.
# Examples
# Input	Output
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00	Mark -> 5.50 2.50 3.46 (avg: 3.82)
# Peter -> 5.20 3.20 (avg: 4.20)
# Alex -> 2.00 3.00 (avg: 2.50)
# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66	Ted -> 3.00 3.66 (avg: 3.33)
# Scott -> 4.50 5.00 (avg: 4.75)
#
# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30	Peter -> 4.40 (avg: 4.40)
# Lee -> 6.00 5.50 6.00 (avg: 5.83)
# Kenny -> 3.30 (avg: 3.30)