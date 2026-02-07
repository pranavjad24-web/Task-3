n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = v

rev = {}
for k in d:
    rev[d[k]] = k

print(rev)
