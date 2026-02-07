a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = False
for i in range(len(a)):
    if a[i:] + a[:i] == b:
        flag = True
        break

print(flag)
