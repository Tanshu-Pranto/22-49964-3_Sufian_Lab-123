import os
import pandas as pd

# Locate Titanic.csv even if the script is run from another folder
base_dir = os.path.dirname(os.path.abspath(__file__))
possible_paths = [
    os.path.join(base_dir, "Titanic.csv"),
    os.path.join(base_dir, "archive", "Titanic.csv"),
    os.path.join(base_dir, "LAB 8", "Titanic.csv")
]

csv_path = next((path for path in possible_paths if os.path.exists(path)), possible_paths[0])

# Load Titanic dataset
try:
    titanic = pd.read_csv(csv_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Titanic dataset was not found. Checked: {possible_paths}")

print("Original Dataset:")
print(titanic.head())

# --------------------------------------------------
# 1. Empty cells / missing values
# --------------------------------------------------
print("\nMissing values before cleaning:")
print(titanic.isnull().sum())

# Fill missing values in categorical columns using mode
for column in ["Embarked"]:
    if column in titanic.columns and titanic[column].isnull().sum() > 0:
        titanic[column] = titanic[column].fillna(titanic[column].mode()[0])

# Fill missing numeric values with median for numeric columns
for column in ["Age", "Fare"]:
    if column in titanic.columns and titanic[column].isnull().sum() > 0:
        titanic[column] = titanic[column].fillna(titanic[column].median())

# --------------------------------------------------
# 2. Wrong format / incorrect data types
# --------------------------------------------------
print("\nData types before cleaning:")
print(titanic.dtypes)

# Convert relevant columns to numeric
numeric_columns = [
    "Passengerid",
    "Age",
    "Fare",
    "Sex",
    "sibsp",
    "Parch",
    "Pclass",
    "Embarked",
    "2urvived"
]

for column in numeric_columns:
    if column in titanic.columns:
        titanic[column] = pd.to_numeric(titanic[column], errors="coerce")

# --------------------------------------------------
# 3. Wrong data / invalid values
# --------------------------------------------------
# Remove negative values for numeric variables
for column in ["Age", "Fare"]:
    if column in titanic.columns:
        titanic.loc[titanic[column] < 0, column] = titanic[column].median()

# Optional: remove rows with invalid values where needed
# Example: if Age is NaN after conversion, fill with median again
if "Age" in titanic.columns:
    titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

if "Fare" in titanic.columns:
    titanic["Fare"] = titanic["Fare"].fillna(titanic["Fare"].median())

# --------------------------------------------------
# 4. Duplicates
# --------------------------------------------------
duplicates = titanic.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)
titanic = titanic.drop_duplicates()

# --------------------------------------------------
# Final result
# --------------------------------------------------
print("\nMissing values after cleaning:")
print(titanic.isnull().sum())

print("\nCleaned Dataset:")
print(titanic.head())

print("\nFinal Dataset Information:")
titanic.info()