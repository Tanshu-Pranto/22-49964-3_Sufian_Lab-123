import numpy as np

arr = np.array([10, -5, 20, -8, 30, -2, 40])

print("Original array:")
print(arr)

arr[arr < 0] = 0

print("\nAfter replacing negative values:")
print(arr)