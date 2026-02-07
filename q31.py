n = int(input())
vocab = set()

for _ in range(n):
    words = input().lower().split()
    for w in words:
        vocab.add(w)

print(vocab)
