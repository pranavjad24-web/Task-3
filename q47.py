scores = list(map(int, input().split()))
rank = 1
prev = None
skip = 0

for s in sorted(scores, reverse=True):
    if s != prev:
        rank += skip
        skip = 0
    print(s, rank)
    skip += 1
    prev = s
