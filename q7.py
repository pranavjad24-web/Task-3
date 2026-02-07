n = int(input())
nested = []

for i in range(n):
    nested.append(list(map(int, input().split())))

flat = []
for row in nested:
    for val in row:
        flat.append(val)

print(flat)
