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