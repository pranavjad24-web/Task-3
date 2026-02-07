config = eval(input())
required = set(input().split())

print("Missing:", required - config.keys())
print("Extra:", config.keys() - required)
