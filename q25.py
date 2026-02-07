r = int(input())
matrix = []

for _ in range(r):
    matrix.append(list(map(int, input().split())))

unique = True
for row in matrix:
    if len(row) != len(set(row)):
        unique = False
        break

print("Unique Rows" if unique else "Not Unique")
