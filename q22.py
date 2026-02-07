nums = list(map(int, input().split()))

even = []
odd = []

for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(even)
print(odd)
