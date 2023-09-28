import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load data
diabetes_data = pd.read_csv("E:\Health Web App\dataset\diabetes.csv")

# Split data into features and target
X = diabetes_data.drop(columns="Outcome", axis=1)
Y = diabetes_data["Outcome"]

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the Logistic Regression Model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, Y_train)

# Calculate accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print("Training Accuracy:", training_data_accuracy)

# Calculate accuracy on testing data
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print("Testing Accuracy:", testing_data_accuracy)

# Save the model
joblib.dump(model, "model_diabetes.pkl")
