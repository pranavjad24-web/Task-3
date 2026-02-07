names = input().split()
marks = list(map(int, input().split()))

data = []
for i in range(len(names)):
    data.append((names[i], marks[i]))

data.sort(key=lambda x: x[1], reverse=True)

rank = 1
for name, mark in data:
    print(name, "Rank:", rank)
    rank += 1
