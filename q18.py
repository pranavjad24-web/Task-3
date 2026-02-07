n = int(input())
students = {}

for _ in range(n):
    name = input()
    marks = list(map(int, input().split()))
    students[name] = marks

avg_dict = {}

for name in students:
    total = 0
    for m in students[name]:
        total += m
    avg_dict[name] = total / len(students[name])

print(avg_dict)
