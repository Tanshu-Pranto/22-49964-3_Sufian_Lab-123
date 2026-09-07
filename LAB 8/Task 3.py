import os
import pandas as pd

# Load Titanic dataset from the same folder as this script
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "Titanic.csv")
titanic = pd.read_csv(csv_path)

# Display first 5 rows
print("First 5 rows:")
print(titanic.head())

# Display last 5 rows
print("\nLast 5 rows:")
print(titanic.tail())

# Display information about dataset
print("\nDataset Information:")
titanic.info()