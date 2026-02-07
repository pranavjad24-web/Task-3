data = list(map(int, input().split()))
remove_list = list(map(int, input().split()))

result = []
for x in data:
    if x not in remove_list:
        result.append(x)

print(result)
