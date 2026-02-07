s = input()

count = {"alphabets": 0, "digits": 0, "special": 0}

for ch in s:
    if ch.isalpha():
        count["alphabets"] += 1
    elif ch.isdigit():
        count["digits"] += 1
    else:
        count["special"] += 1

print(count)
