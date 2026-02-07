r = int(input("Enter number of rows: "))
matrix = []

for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    row_max = row[0]
    for val in row:
        if val > row_max:
            row_max = val
    print(row_max)
