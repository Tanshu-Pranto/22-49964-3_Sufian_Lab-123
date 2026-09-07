import os
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Load Titanic dataset
# --------------------------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
paths = [
    os.path.join(base_dir, "Titanic.csv"),
    os.path.join(base_dir, "..", "archive", "Titanic.csv"),
    os.path.join(base_dir, "..", "LAB 8", "Titanic.csv")
]

csv_path = next((p for p in paths if os.path.exists(p)), paths[0])
df = pd.read_csv(csv_path)

print("Titanic dataset loaded successfully!")
print(df.head())

# --------------------------------------------------
# 1. Line plot
# --------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(df.index[:50], df["Age"].head(50), marker="o", linestyle="-", color="royalblue")
plt.title("Line Plot of Age for the First 50 Passengers")
plt.xlabel("Passenger Index")
plt.ylabel("Age")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 2. Scatter plot
# --------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Fare"], alpha=0.6, color="darkgreen")
plt.title("Scatter Plot: Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 3. Bar chart
# --------------------------------------------------
class_counts = df["Pclass"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
class_counts.plot(kind="bar", color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Bar Chart: Number of Passengers by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 4. Histogram
# --------------------------------------------------
plt.figure(figsize=(8, 5))
df["Age"].plot(kind="hist", bins=20, color="steelblue", edgecolor="black")
plt.title("Histogram of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 5. Pie chart
# --------------------------------------------------
labels = ["Did Not Survive", "Survived"]
survival_counts = df["2urvived"].value_counts().sort_index()
values = [survival_counts.get(0, 0), survival_counts.get(1, 0)]

plt.figure(figsize=(7, 7))
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=["#D95F02", "#1B9E77"])
plt.title("Pie Chart: Survival Distribution")
plt.axis("equal")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 6. Subplots
# --------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Age histogram
axes[0, 0].hist(df["Age"], bins=20, color="skyblue", edgecolor="black")
axes[0, 0].set_title("Age Distribution")
axes[0, 0].set_xlabel("Age")
axes[0, 0].set_ylabel("Frequency")

# Fare histogram
axes[0, 1].hist(df["Fare"], bins=20, color="lightcoral", edgecolor="black")
axes[0, 1].set_title("Fare Distribution")
axes[0, 1].set_xlabel("Fare")
axes[0, 1].set_ylabel("Frequency")

# Bar chart by sex
sex_counts = df["Sex"].value_counts().sort_index()
axes[1, 0].bar(["Male", "Female"], [sex_counts.get(0, 0), sex_counts.get(1, 0)], color=["#4E79A7", "#F28E2B"])
axes[1, 0].set_title("Passenger Count by Sex")
axes[1, 0].set_xlabel("Sex")
axes[1, 0].set_ylabel("Count")

# Survival bar chart
survival_bar = df["2urvived"].value_counts().sort_index()
axes[1, 1].bar(["Not Survived", "Survived"], [survival_bar.get(0, 0), survival_bar.get(1, 0)], color=["#B07AA1", "#59A14F"])
axes[1, 1].set_title("Survival Count")
axes[1, 1].set_xlabel("Survival")
axes[1, 1].set_ylabel("Count")

plt.tight_layout()
plt.show()

print("All Titanic visualizations completed successfully.")
