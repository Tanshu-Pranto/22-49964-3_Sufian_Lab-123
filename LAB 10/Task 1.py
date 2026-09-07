import numpy as np

arr = np.array([12, 5, 8, 1, 19, 3])

k = 3

smallest = np.sort(arr)[:k]

print("The", k, "smallest values are:")
print(smallest)