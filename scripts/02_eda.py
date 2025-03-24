import pandas as pd

df = pd.read_csv("outputs/cleaned_data.csv")

summary = df.describe(include='all')
summary.to_csv("outputs/summary_statistics.csv")

categoricals = ['gender', 'counseling_attendance', 'family_mental_health_history', 'medical_condition']
for col in categoricals:
    df[col].value_counts().to_csv(f"outputs/{col}_value_counts.csv")
