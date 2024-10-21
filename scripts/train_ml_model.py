from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Example data
data = {
    'code_churn': [100, 50, 200, 30],
    'test_coverage': [80, 90, 70, 60],
    'build_success': [1, 1, 0, 0]
}
df = pd.DataFrame(data)

X = df[['code_churn', 'test_coverage']]
y = df['build_success']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save trained model
import pickle
with open('models/trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model accuracy:", model.score(X_test, y_test))
