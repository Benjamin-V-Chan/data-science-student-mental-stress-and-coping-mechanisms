import pandas as pd

df = pd.read_csv("outputs/cleaned_data.csv")

df = pd.get_dummies(df, columns=['gender', 'counseling_attendance', 
                                 'family_mental_health_history', 'medical_condition'], drop_first=True)

df['high_stress'] = (df['mental_stress_level'] >= 7).astype(int)

df.to_csv("outputs/featured_data.csv", index=False)
