nums = list(map(int, input().split()))

min_v = nums[0]
max_v = nums[0]
total = 0

for n in nums:
    if n < min_v:
        min_v = n
    if n > max_v:
        max_v = n
    total += n

avg = total / len(nums)

print((min_v, max_v, avg))
