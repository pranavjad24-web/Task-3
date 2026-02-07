n = int(input())
pairs = []

for _ in range(n):
    a, b = map(int, input().split())
    if (b, a) not in pairs:
        pairs.append((a, b))

print(pairs)
