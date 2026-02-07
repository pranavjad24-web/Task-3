words = input().split()
d = {}

for w in words:
    l = len(w)
    d.setdefault(l, []).append(w)

print(d)
