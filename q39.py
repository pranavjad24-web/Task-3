nums = list(map(int, input().split()))
k = int(input())

freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

result = sorted(freq, key=freq.get, reverse=True)[:k]
print(result)
