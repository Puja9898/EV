import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 📂 Load Sample Dataset (Replace with actual data)
data = pd.DataFrame({
    "acceleration": [1.2, 15.8, 3.1, 16.0, 2.5, 14.5],
    "gyroscope": [0.5, 7.8, 1.0, 8.2, 0.7, 7.1],
    "movement": [1, 0, 1, 0, 1, 0],
    "crash_impact": [0, 1, 0, 1, 0, 1],
    "accident": [0, 1, 0, 1, 0, 1]  # Target variable (1 = accident, 0 = no accident)
})

# 🏋️ Split Data into Training and Testing
X = data.drop(columns=["accident"])  # Features
y = data["accident"]  # Labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🚀 Train Machine Learning Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🎯 Test Accuracy
y_pred = model.predict(X_test)
print("✅ Model Accuracy:", accuracy_score(y_test, y_pred))

# 💾 Save Model as `accident_model.pkl`
joblib.dump(model, "accident_model.pkl")
print("📁 Model saved as accident_model.pkl")
