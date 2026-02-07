n = int(input())
d = {}
res = {}

for _ in range(n):
    s, dept = input().split()
    d[s] = dept

for s in d:
    res.setdefault(d[s], []).append(s)

print(res)
