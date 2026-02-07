nums = list(map(int, input().split()))
leaders = []

for i in range(len(nums)):
    is_leader = True
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            is_leader = False
            break
    if is_leader:
        leaders.append(nums[i])

print(leaders)
