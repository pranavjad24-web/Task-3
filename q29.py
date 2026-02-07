n = int(input())
freq = {}

for _ in range(n):
    t = tuple(map(int, input().split()))
    freq[t] = freq.get(t, 0) + 1

print(freq)
