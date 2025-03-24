import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("outputs/cleaned_data.csv")

numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.savefig(f"outputs/hist_{col}.png")
    plt.close()

plt.figure()
sns.boxplot(x='high_stress', y='sleep_duration_hours_per_night', data=df.assign(high_stress=(df['mental_stress_level'] >= 7).astype(int)))
plt.title("Sleep Duration vs High Stress")
plt.savefig("outputs/box_sleep_vs_stress.png")
plt.close()
