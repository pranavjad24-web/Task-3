expected = set(input().split())
docs = input().lower().split()

used = set(docs)
covered = expected & used

percent = (len(covered) / len(expected)) * 100
print(percent)
print(expected - used)
