import pandas as pd

df = pd.read_csv("data/student_stress.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

df.dropna(inplace=True)

df['gender'] = df['gender'].str.title()
df['counseling_attendance'] = df['counseling_attendance'].str.strip().str.capitalize()
df['family_mental_health_history'] = df['family_mental_health_history'].str.strip().str.capitalize()
df['medical_condition'] = df['medical_condition'].str.strip().str.capitalize()

df.to_csv("outputs/cleaned_data.csv", index=False)
