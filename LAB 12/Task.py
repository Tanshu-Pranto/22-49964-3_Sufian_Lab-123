from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


dataset_path = Path(__file__).with_name("diabetes_prediction_dataset.csv")
data = pd.read_csv(dataset_path)

features = data.drop(columns="diabetes")
target = data["diabetes"]

# Convert the categorical columns to numeric features for scikit-learn.
features = pd.get_dummies(features, drop_first=True)

features_train, features_test, target_train, target_test = train_test_split(
	features,
	target,
	test_size=0.2,
	random_state=42,
	stratify=target,
)

scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)

model = DecisionTreeClassifier(random_state=42)
model.fit(features_train, target_train)

predictions = model.predict(features_test)
accuracy = accuracy_score(target_test, predictions)

print(f"Dataset shape: {data.shape}")
print(f"Test accuracy: {accuracy:.4f}")
