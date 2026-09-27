# Assignments
# Exercise 1: Train a Model

from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy of the Decision Tree model: {accuracy:.2%}")
print(f"{'*'*60}")



# Exercise 2: Make Predictions
import numpy as np

# Sample data for prediction
sample_data = np.array([[5.1, 3.5, 1.4, 0.2],  # Example of Iris Setosa
                        [6.7, 3.1, 4.7, 1.5],  # Example of Iris Versicolor
                        [7.2, 3.6, 6.1, 2.5]])  # Example of Iris Virginica
model_predictions = model.predict(sample_data)
names = load_iris().target_names
print("\nPredictions for the sample data:")
for i, prediction in enumerate(model_predictions):
    print(f"Sample {i+1}: Predicted class - {names[prediction]}")
print(f"{'*'*60}")



# Exercise 3: Feature Importance
feature_importance = model.feature_importances_
print(f"\nFeature Importance:")
for i, importance in enumerate(feature_importance):
    print(f"Feature {i+1}: {importance:.2%}")
print(f"{'*'*60}")




# Exercise 4: Challenge
from sklearn.linear_model import LogisticRegression
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression(max_iter=10000).fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"\nAccuracy of the Logistic Regression model on Breast Cancer dataset: {accuracy:.2%}")
print(f"{'*'*60}")



# Exercise 5: Trade Application — Construction Project Risk Assessment
def predict_delivery_risk(crew_size, days_remaining, task_left):
    # effeciency: task per worker per day needed to complete the project
    efficiency = task_left / (crew_size * days_remaining)
    if efficiency > 1.5:
        return "High Risk of Delay, require more resources or time"
    elif efficiency > 0.8:
        return "Moderate Risk of Delay, don't waste time"
    else:
        return "Low Risk of Delay, project is on track"

projects = [
    ("Land plowing", 3, 5, 25),
    ("Pit digging", 4, 10, 18),
    ("Constracting latrine", 2, 3, 12),
]

for name, crew, days, task in projects:
    risk = predict_delivery_risk(crew, days, task)
    print(f"\n{name})")
    print(f"Crew size: {crew} | Days remaining: {days} | Task left: {task}")
    print(f"Risk Assessment: {risk}")
print(f"{'*'*60}\n")    




# Exercise 6: Farming Application — Goat Health Risk Predictor
def predict_goat_health(name,weight_loss_kg, age, feed_drop_pct):
    risk_score = 0
    if weight_loss_kg > 3:
        risk_score +=2
    elif weight_loss_kg > 1.5:
        risk_score +=1
    if feed_drop_pct > 30:
        risk_score +=2
    elif feed_drop_pct > 15:
        risk_score +=1
    if age > 8:
        risk_score +=1

    if risk_score > 4:
        return "High risk: call vet"
    elif risk_score > 2:
        return "Medium risk: minitor closely"
    else:
        return "Low risk: healthy"

# data of 5 goats
goats = [
    ('Simba', 4.2, 35, 3),
    ('Kijana', 0.5, 8, 2),
    ('Mzee', 2.1, 20, 9),
    ('Dama', 3.8, 40, 3),
    ('Furaha', 0.8, 10, 4)
]
print("Goat Health Assessment")
print(f"{'-'*45}")

for name, weight, age, feed in goats:
    result = predict_goat_health(name, weight, age, feed)
    print(f"{name}: weight loss {weight}kg | feed drop {feed}% | age {age}yrs")
    print(f"  Assessment {result}\n")
print(f"{'*'*60}")  