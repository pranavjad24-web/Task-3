text = input().lower().split()
unique = set()

for word in text:
    unique.add(word)

print(len(unique))
