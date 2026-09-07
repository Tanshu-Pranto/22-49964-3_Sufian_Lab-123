import numpy as np

arr = np.array([10, 20, 30, 20, 40, 20, 50, 20])

value = 20
n = 3

positions = np.where(arr == value)[0]

if len(positions) >= n:
    print("Index of", n, "rd occurrence of", value, "is:", positions[n - 1])
else:
    print("The value does not occur", n, "times.")