nums = list(map(int, input().split()))
pairs = []

for n in nums:
    pairs.append((n, n*n))

print(pairs)
