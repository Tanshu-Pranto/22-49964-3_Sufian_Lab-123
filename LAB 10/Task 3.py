import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Array:")
print(arr)

column_sum = np.sum(arr, axis=0)
row_sum = np.sum(arr, axis=1)

print("\nColumn sums:")
print(column_sum)

print("\nRow sums:")
print(row_sum)