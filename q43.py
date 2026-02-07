n = int(input())
records = []
dup = False

for _ in range(n):
    r = eval(input())
    if r in records:
        dup = True
    records.append(r)

print(dup)
