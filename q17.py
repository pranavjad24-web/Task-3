a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []

for x in a:
    if x not in b:
        result.append(x)

for x in b:
    if x not in a:
        result.append(x)

print(result)
