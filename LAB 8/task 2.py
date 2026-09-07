import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("\nRows 0 and 2:")
print(df.loc[[0, 2]])