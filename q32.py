nums = list(map(int, input().split()))
seen = set()
dup = False

for n in nums:
    if n in seen:
        dup = True
        break
    seen.add(n)

print(dup)
