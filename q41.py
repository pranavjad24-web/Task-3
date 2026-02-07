n = int(input())
res = {}

for _ in range(n):
    name = input()
    marks = int(input())
    att = int(input())
    res[name] = marks*0.7 + att*0.3

topper = max(res, key=res.get)
print(res)
print("Topper:", topper)
