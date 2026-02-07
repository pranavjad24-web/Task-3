num = input()
digits = set(num)

missing = []
for i in range(10):
    if str(i) not in digits:
        missing.append(i)

print(missing)
