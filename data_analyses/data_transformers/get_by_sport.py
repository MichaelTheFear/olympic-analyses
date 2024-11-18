import pandas as pd

columns = ['Age', 'Height', 'BMI', 'GDP', 'Sport']
df = pd.read_csv("../data/features.csv")
df = df[columns]
aggregated_df = df.groupby('Sport', as_index=False).mean()
aggregated_df.to_csv("../data/by_sport.csv", index=False)