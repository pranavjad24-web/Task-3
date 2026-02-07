n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

primary = 0
secondary = 0

for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n-i-1]

print(primary, secondary)
