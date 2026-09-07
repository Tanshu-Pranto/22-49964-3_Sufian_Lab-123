import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original array:")
print(arr)

new_arr = arr.reshape(2, 3)

print("\nNew shape:")
print(new_arr)