n = int(input())
d1 = {}
d2 = {}

for _ in range(n):
    k, v = input().split()
    d1[k] = int(v)

for _ in range(n):
    k, v = input().split()
    d2[k] = int(v)

res = {}
for k in d1:
    res[k] = d1[k] + d2[k]

print(res)
