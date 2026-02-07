rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

col_sum = []

for j in range(cols):
    s = 0
    for i in range(rows):
        s += matrix[i][j]
    col_sum.append(s)

print("Column-wise sum:", col_sum)
