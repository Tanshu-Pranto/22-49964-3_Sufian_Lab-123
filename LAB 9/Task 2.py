import numpy as np

arr = np.array([10, 20, 30, 20, 50, 20])

value = 20

positions = np.where(arr == value)

print("Positions of", value, ":")
print(positions[0])