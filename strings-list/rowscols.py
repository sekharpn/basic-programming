rows, cols = 5, 10

mat = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]]

print("Displaying in the matrix form:")

for i in range(rows):
    print("\nrow#", i, "   ==>   ", end=' ')
    for j in range(cols):
        print(mat[i][j], end='\t')

colsum = [0] * cols  # Creating a new list of zeros of size 10
for j in range(cols):
    for i in range(rows):
        colsum[j] += mat[i][j]  # Calculating sum of each column value and assi

print("\n\nColumn Sums are:", colsum)