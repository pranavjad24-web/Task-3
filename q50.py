n = int(input())
rows = []
keys = set()

for _ in range(n):
    r = eval(input())
    rows.append(r)
    keys.update(r.keys())

unique = {}
for k in keys:
    unique[k] = len({r[k] for r in rows if k in r})

print({"rows": n, "unique_values": unique})
