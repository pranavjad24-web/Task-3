nums = list(map(int, input().split()))

max_len = 1
curr = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
        curr += 1
        if curr > max_len:
            max_len = curr
    else:
        curr = 1

print(max_len)
