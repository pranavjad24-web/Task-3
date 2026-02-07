n = int(input())
keys = None
consistent = True

for _ in range(n):
    d = eval(input())
    if keys is None:
        keys = set(d.keys())
    elif set(d.keys()) != keys:
        consistent = False

print("Consistent" if consistent else "Not Consistent")
