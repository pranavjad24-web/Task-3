nums = list(map(int, input().split()))
k = int(input())

n = len(nums)
k = k % n   

rotated = []

for i in range(n - k, n):
    rotated.append(nums[i])

for i in range(0, n - k):
    rotated.append(nums[i])

print(rotated)
