a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

common = []
for x in a:
    if x in b and x in c and x not in common:
        common.append(x)

print(common)
