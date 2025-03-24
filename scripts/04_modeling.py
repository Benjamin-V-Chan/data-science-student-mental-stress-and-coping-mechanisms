import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("outputs/featured_data.csv")

X = df.drop(columns=['student_id', 'mental_stress_level', 'stress_coping_mechanisms', 'high_stress'])
y = df['high_stress']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

pd.DataFrame(report).transpose().to_csv("outputs/classification_report.csv")
with open("outputs/accuracy.txt", "w") as f:
    f.write(f"Accuracy: {accuracy}")
