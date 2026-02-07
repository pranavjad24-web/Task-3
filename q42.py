n = int(input())
dept = {}

for _ in range(n):
    name, d, marks = input().split()
    marks = int(marks)
    if d not in dept or dept[d][1] < marks:
        dept[d] = (name, marks)

print(dept)
